import re
import unicodedata
from copy import copy
from io import BytesIO
from urllib.parse import quote_plus

import cbor2
import cwt
from base45 import b45encode, b45decode
import qrcode
from pydantic import BaseModel
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask

from app.errors import CannotSignInvalidIssuer, TagsError
from app.log import logger
from settings import conf
from testdata import INVALID_KEY_DATA, DUMMY_JWK

# COSE algorithms from technical format to string argment format
# https://python-cwt.readthedocs.io/en/stable/algorithms.html#cose-algorithms
ALGS = {
    -257: "RS256"
}

RSA_PRIVATE_KEY = cwt.COSEKey.from_pem(key_data=conf.RSA_PRIVATE_KEY, alg="RS256", kid=conf.RSA_KID)
INVALID_PRIVATE_KEY = cwt.COSEKey.from_pem(key_data=INVALID_KEY_DATA, alg="RS256", kid=conf.RSA_KID)

# Version prefix for all tags
IOXIO_TAGS_HEADER = "IT1:".encode("utf-8")

CORRECTIONS = {
    "L": qrcode.ERROR_CORRECT_L,
    "M": qrcode.ERROR_CORRECT_M,
    "Q": qrcode.ERROR_CORRECT_Q,
    "H": qrcode.ERROR_CORRECT_H,
}


class CodePayload(BaseModel):
    iss: str
    product: str
    id: str


class CodeBasics(BaseModel):
    payload: CodePayload
    alg: str
    kid: str


async def fetch_json_file(url: str) -> dict:
    raise NotImplementedError()


def parse_code_insecure(code: str) -> CodeBasics:
    if code.startswith("IT1:"):
        code_b45 = code[4:]
    else:
        raise TagsError(
            error="Not an IOXIO Tag code, missing version identifier.",
            code="signature_verification_failed",
        )

    try:
        cose_bytes = b45decode(code_b45)
    except ValueError:
        raise TagsError(
            error="Not an IOXIO Tag code, failed Base45 decode",
            code="signature_verification_failed",
        )

    msg = cwt.COSEMessage.loads(cose_bytes)

    # Extract alg and Key ID
    alg = ALGS[msg.protected[1]]
    kid = msg.unprotected[4]

    # Pretend like we have a key for this code
    dummy_jwk = copy(DUMMY_JWK)
    dummy_jwk["kid"] = kid
    dummy_jwk["alg"] = alg

    dummy_key = cwt.COSEKey.from_jwk(dummy_jwk)
    # Override "verify" to always say it is ok
    dummy_key.verify = lambda x, y: True

    try:
        payload = cwt.decode(cose_bytes, dummy_key, no_verify=True)
        return CodeBasics(
            alg=alg,
            kid=kid,
            payload=CodePayload(**payload)
        )
    except cwt.CWTError as e:
        raise TagsError(
            error=str(e),
            code="signature_verification_failed",
        )


async def verify_code(code_b45: str):
    basics = parse_code_insecure(code_b45)

    # TODO: Fetch files, actually verify contents


def slugify(value: str, allow_unicode=False) -> str:
    """
    Based on https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, dots, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^.\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def make_image_filename(iss: str, product: str, id: str, security: str) -> str:
    return f"{slugify(iss)}_{slugify(product)}_{slugify(id)}_{slugify(security)}.png"


def make_image(payload: bytes, frame_type: str) -> bytes:
    qr = qrcode.QRCode(error_correction=CORRECTIONS[conf.QR_CORRECTION_LEVEL])
    qr.add_data(payload)

    img = qr.make_image(
        color_mask=SolidFillColorMask(
            front_color=conf.QR_FOREGROUND,
            back_color=conf.QR_BACKGROUND,
        ),
        image_factory=StyledPilImage,
    )

    # TODO: Wrap in frame using cairosvg + pillow

    # Get image contents as bytes
    container = BytesIO()
    img.save(container)
    return container.getvalue()


def make_cose_code(iss: str, product: str, id: str, valid: bool) -> (str, bytes):
    if valid:
        if iss != conf.RSA_ISS:
            raise CannotSignInvalidIssuer()
        private_key = RSA_PRIVATE_KEY
    else:
        private_key = INVALID_PRIVATE_KEY

    if valid:
        logger.info(f"Making a COSE signed IOXIO Tag for iss {iss}, product {product}, id {id}, with a valid signature")
    else:
        logger.info(
            f"Making a COSE signed IOXIO Tag for iss {iss}, product {product}, id {id}, with an invalid signature")

    raw_data = {
        "iss": iss,
        "product": product,
        "id": id,
    }

    cbor_data = cbor2.dumps(raw_data)
    cose = cwt.COSE(alg_auto_inclusion=True, kid_auto_inclusion=True)
    cose_encoded = cose.encode(cbor_data, private_key)
    payload = IOXIO_TAGS_HEADER + b45encode(cose_encoded)

    if valid:
        filename = make_image_filename(iss, product, id, "signed")
    else:
        filename = make_image_filename(iss, product, id, "invalid")

    return filename, make_image(payload, "secure")


def make_url_code(iss: str, product: str, id: str) -> (str, bytes):
    logger.info(f"Making a simple IOXIO Tag for iss {iss}, product {product}, id {id}, in URL format")

    url = "https://tags.ioxio.dev/q/"
    url += "/".join([
        quote_plus(iss),
        quote_plus(product),
        quote_plus(id),
    ])

    filename = make_image_filename(iss, product, id, "simple")
    return filename, make_image(url.encode("utf-8"), "simple")