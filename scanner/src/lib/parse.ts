import { decode as decodeCbor } from "cbor-x"
import { Buffer } from "buffer"
import { decode as decodeBase45 } from "base45"
import { consoleLog } from "./common"

// Very uncool way of trying to fix the low quality library
if (typeof window !== "undefined") {
  if (window.Buffer === undefined) {
    window.Buffer = Buffer
  }
}

const PRESET_JWKS = {
  keys: [
    {
      alg: "RS256",
      kid: "01",
      kty: "RSA",
      n:
        "yicAxwnv46tR82buQHN2b2dDLOmZ0iJYR6GPwNOShlCdN-N5N6spvAbe3UNb6ymN8AtW5o9_6Rm6gpungvlnDtjyZfPnNzAryjR8Z1" +
        "Jvb33spr7zcLWG8TzL1l5r5b2zMnWXaDOZffAxa3SWZ14ZufAAA97fW3oBJXYr4H0zB8aFNuPDtYw4puN4s3M1vQH6OPgXDkSNYBv5Zbx" +
        "lKasPXdFf_fXA9u4p9JMmtNS3fL7RibMqbrf4jCkATwVqA_Ui9vlgudZeHqW0tpzuXT3FVyVN-eFQwq6Hk3vY8iqRD9Skbpol9vHQLKY8" +
        "px5tZZTxVtNcLhTKzNToMWQMykuq0Q",
      e: "AQAB",
    },
  ],
}

const IOXIO_TAGS_VERSION_PREFIX = "IT1:"

type RawSecureTagParseResult = {
  kid: string // JWKS key ID
  payload: {
    iss: string // Issuer domain
    product: string // Generic product name / category
    id: string // Unique ID of the product
  }
}

function isTagsURL(url: string) {
  const urlPattern = /https:\/\/tags\.ioxio\.(dev|io)\/.*$/
  return urlPattern.test(url)
}

function stringToBuffer(value: string): Buffer {
  return Buffer.from(value)
}

function Uint8ArrayToString(value: Uint8Array): string {
  return new TextDecoder().decode(value)
}

async function parseCoseInsecure(message: Buffer): Promise<RawSecureTagParseResult> {
  // No verification of signature performed here
  const coseContainer = decodeCbor(message)
  const [_headers1, _headers2, cborPayload, _signature] = coseContainer.value

  consoleLog(JSON.stringify({ _headers1, _headers2, cborPayload, _signature }))

  // Extract key ID from headers
  // https://www.iana.org/assignments/cose/cose.xhtml
  const kid = Uint8ArrayToString(_headers2[4])

  return {
    kid: kid,
    payload: decodeCbor(cborPayload),
  }
}

async function verifyCose(message: Buffer, jwk: object): Promise<boolean> {
  consoleLog(`Verifying: ${message} with ${JSON.stringify(jwk)}`)

  // cose-js library uses `require` etc. and doesn't seem to actually work in a browser for multiple reasons
  // @mattrglobal/cose might work but their licensing is not compatible with .. anything
  // might just have to submit this to a backend, maybe running Node, maybe running Python
  consoleLog("Cannot verify COSE yet")
  throw new Error("Cannot verify COSE yet")

  return true
}

export async function tryParseIoxioTags(contents: string): Promise<boolean> {
  const isValidURL = isTagsURL(contents)
  if (isValidURL) {
    consoleLog("Found low security IOXIO Tag URL")
    consoleLog(contents)
    return true
  } else {
    consoleLog("Didn't scan an IOXIO Tag URL, maybe it's B45-COSE?", "warn")
    consoleLog(contents, "warn")
    try {
      if (contents.startsWith(IOXIO_TAGS_VERSION_PREFIX)) {
        const withoutVersion = contents.substring(IOXIO_TAGS_VERSION_PREFIX.length)
        const b45decoded = decodeBase45(withoutVersion)
        const cborData = await parseCoseInsecure(b45decoded)
        consoleLog("Parsed insecure data:" + cborData, "info")
        if (
          cborData.kid &&
          cborData.payload.iss &&
          cborData.payload.product &&
          cborData.payload.id
        ) {
          // This is an IOXIO Tags QR code
          consoleLog("IOXIO Tag detected, should continue to do more things")
          consoleLog(JSON.stringify(cborData.payload))

          // TODO: Fetch metadata + JWKS keys from cborData.iss
          // TODO: Verify COSE signature with JWKS key
          // TODO: Display available data products based on metadata

          // Instead right now just trying against preset key
          const jwk = PRESET_JWKS.keys.find((key) => {
            return key.kid === cborData.kid
          })

          let verified = false

          if (!jwk) {
            consoleLog("Couldn't find the JWKS key to verify this code", "warn")
          } else {
            verified = await verifyCose(b45decoded, jwk)
          }

          return true
        }
      } else {
        // No IT1: prefix
        return false
      }
    } catch (e: any) {
      if (e.toString().indexOf("Invalid base45 string") !== -1) {
        // TODO: Show error
        consoleLog(`Not a valid IOXIO Tag: ${contents}`, "warn")
      } else {
        // TODO: Show error
        consoleLog(e, "warn")
        return false
      }
    }
  }
}
