import { decode as decodeCbor } from "cbor-x"
import { Buffer } from "buffer"
import { decode as decodeBase45 } from "base45"
import { consoleLog } from "./common"
import { tag } from "./api"
import type { components } from "./openapi"

// Very uncool way of trying to fix the low quality library
if (typeof window !== "undefined") {
  if (window.Buffer === undefined) {
    window.Buffer = Buffer
  }
}

const IOXIO_TAGS_VERSION_PREFIX = "IT1:"
// /q/{iss}/{product}/{id}
const IOXIO_URL_REGEX = /\/q\/([^/]+)\/([^/]+)\/([^/]+)/

export type Payload = {
  iss: string // Issuer domain
  product: string // Generic product name / category
  id: string // Unique ID of the product
  verified: boolean // Verification status
  error?: string // Error message
}

type RawSecureTagParseResult = {
  kid: string // JWKS key ID
  payload: Payload
}

function isTagsURL(url: string) {
  const urlPattern = /https:\/\/tags\.ioxio\.(dev|io)\/q\/.*$/
  return urlPattern.test(url)
}

// function stringToBuffer(value: string): Buffer {
//   return Buffer.from(value)
// }

function Uint8ArrayToString(value: Uint8Array): string {
  return new TextDecoder().decode(value)
}

async function parseCoseInsecure(message: Buffer): Promise<RawSecureTagParseResult> {
  // No verification of signature performed here
  const coseContainer = decodeCbor(message)

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const [_headers1, _headers2, cborPayload, _signature] = coseContainer.value

  // Extract key ID from headers
  // https://www.iana.org/assignments/cose/cose.xhtml
  const kid = Uint8ArrayToString(_headers2[4])

  return {
    kid: kid,
    payload: decodeCbor(cborPayload),
  }
}

export async function tryParseIoxioTags(contents: string): Promise<Payload | undefined> {
  const isValidURL = isTagsURL(contents)
  if (isValidURL) {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    const [_, iss, product, id] = Array.prototype.slice.apply(contents.match(IOXIO_URL_REGEX))
    const payload = { iss, product, id, verified: true }
    return payload
  } else {
    try {
      if (contents.startsWith(IOXIO_TAGS_VERSION_PREFIX)) {
        const withoutVersion = contents.substring(IOXIO_TAGS_VERSION_PREFIX.length)
        const b45decoded = decodeBase45(withoutVersion)
        const cborData = await parseCoseInsecure(b45decoded)
        if (
          cborData.kid &&
          cborData.payload.iss &&
          cborData.payload.product &&
          cborData.payload.id
        ) {
          // This is an IOXIO Tags QR code
          // TODO: verify the signature in `contents` with `/tag/verify/v1`
          // TODO: if verification fails, ask for user to confirm if they want to continue anyway
          const verifyV1 = await tag.tagVerifyV1({ code: contents }).result
          let error: string
          if (verifyV1.status === 400) {
            const data = verifyV1.data as components["schemas"]["TagsErrorResponse"]
            error = data.error
          } else if (verifyV1.status === 422) {
            const data = verifyV1.data as components["schemas"]["HTTPValidationError"]
            error = data.detail?.[0].msg || ""
          } else {
            return {
              ...cborData.payload,
              verified: true,
            }
          }
          return {
            ...cborData.payload,
            verified: false,
            error,
          }
        }
      } else {
        // No IT1: prefix
        return undefined
      }
    } catch (e: unknown) {
      if (e.toString().indexOf("Invalid base45 string") !== -1) {
        // TODO: Show error
        consoleLog(`Not a valid IOXIO Tag: ${contents}`, "warn")
      } else {
        // TODO: Show error
        consoleLog(e, "warn")
        return undefined
      }
    }
  }
}
