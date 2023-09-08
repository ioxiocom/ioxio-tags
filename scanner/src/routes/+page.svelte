<script lang="ts">
  import { decode as decodeCbor } from "cbor-x"
  import { BarcodeScanner } from "@capacitor-community/barcode-scanner"
  import { Buffer } from "buffer"
  import { decode as decodeBase45 } from "base45"

  let scanning = false

  // Pregenerated data for testing
  const PRESET_DATA =
    "IT1:RRQ5 8/60V500GKOG8WA6CADOPCZQE..E6$CPQEGPCKI91/DXPE6$CSED -DUPCH$DV9EV3E $EQWEI93IEC7WEALE4W5" +
    "646D4FPX54%E5$CQX56%E:JC%JCPVC:P4WZCK-CM.CCA7H*6RW67W5VF6CA7XJC3UCAX57079460DCZX61:6256V50PEHZRA9A81+NMXJ0C76BJ" +
    "SUC**B1.VDCMQCKU47AZM52UW1K21R0VB6R55F2CXB/94+SS KBY92RZMO313+P1-O44PFWFB3BYELI.BHAW%2V2*4-AEGB0GX628CCJS1OBAU0" +
    "NH800JDD7UYPH+UNWL1KMH:UMAS4QK:R7$.36QVO8S5YA6SRW1LFA90H7.177ZM7QQ%HVZ 0VHLJQR%VLIPU/NJO68HZNA4PA32K9153Q8EW/%P" +
    "EKBRBNJO3ATK1WEW+P-PL.R0%MQJVTL68+FMLOFRAJ0IHR6W882.8B:EBEG24X74H9COJ:.1C89WFCL M+.C1XJ$Z3PM5OM754GL22D7TVXV*JH" +
    "/X1U66+CHCEMXI0P274GSM.6. LBDD"

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

  // TODO: On mobile devices where permissions allow for it, we should directly start scanning
  async function startScan() {
    // Check camera permission
    // This is just a simple example, check out the better checks below
    await BarcodeScanner.checkPermission({ force: true })

    // make background of WebView transparent
    // note: if you are using ionic this might not be enough, check below
    BarcodeScanner.hideBackground()

    const result = await BarcodeScanner.startScan() // start scanning and wait for a result

    // If the result has content
    if (result.hasContent) {
      const detected = await tryParseIoxioTags(result.content)

      if (detected) {
        // Stop scanning
        console.log("Detected IOXIO Tag")
      } else {
        console.log("No IOXIO Tag detected")
        // TODO: This should just continue scanning
        scanning = false
      }
    }
  }

  async function scanPreset() {
    const detected = await tryParseIoxioTags(PRESET_DATA)
    if (detected) {
      console.log("Detected IOXIO Tag")
    } else {
      console.log("No IOXIO Tag detected")
    }
  }

  function isTagsURL(url: string) {
    const urlPattern = /https:\/\/tags\.ioxio\.(dev|io)\/.*$/
    return urlPattern.test(url)
  }

  async function tryParseIoxioTags(contents: string): Promise<boolean> {
    const isValidURL = isTagsURL(contents)
    if (isValidURL) {
      console.log("Found low security IOXIO Tag URL")
      console.log(contents)
      return true
    } else {
      console.log("Didn't scan an IOXIO Tag URL, maybe it's B45-COSE?")
      console.log(contents)
      try {
        if (contents.startsWith(IOXIO_TAGS_VERSION_PREFIX)) {
          const withoutVersion = contents.substring(IOXIO_TAGS_VERSION_PREFIX.length)
          const b45decoded = decodeBase45(withoutVersion)
          const cborData = await parseCoseInsecure(b45decoded)
          console.log(cborData)
          if (
            cborData.kid &&
            cborData.payload.iss &&
            cborData.payload.product &&
            cborData.payload.id
          ) {
            // This is an IOXIO Tags QR code
            console.log("IOXIO Tag detected, should continue to do more things")

            // TODO: Fetch metadata + JWKS keys from cborData.iss
            // TODO: Verify COSE signature with JWKS key
            // TODO: Display available data products based on metadata

            // Instead right now just trying against preset key
            const jwk = PRESET_JWKS.keys.find((key) => {
              return key.kid === cborData.kid
            })

            let verified = false

            if (!jwk) {
              console.error("Couldn't find the JWKS key to verify this code")
            } else {
              verified = await verifyCose(b45decoded, jwk)
            }

            return true
          }
        } else {
          // No IT1: prefix
          return false
        }
      } catch (e) {
        if (e.toString().indexOf("Invalid base45 string") !== -1) {
          // TODO: Show error
          console.warn(`Not a valid IOXIO Tag: ${contents}`)
        } else {
          // TODO: Show error
          console.error(e)
          return false
        }
      }
    }
  }

  function stringToBuffer(value: string): Buffer {
    return Buffer.from(value)
  }

  function Uint8ArrayToString(value: Uint8Array): string {
    return new TextDecoder().decode(value)
  }

  async function parseCoseInsecure(message: string): Promise<RawSecureTagParseResult> {
    // No verification of signature performed here
    const messageBuffer = stringToBuffer(message)

    const coseContainer = decodeCbor(messageBuffer)
    const [_headers1, _headers2, cborPayload, _signature] = coseContainer.value

    console.log({ _headers1, _headers2, cborPayload, _signature })

    // Extract key ID from headers
    // https://www.iana.org/assignments/cose/cose.xhtml
    const kid = Uint8ArrayToString(_headers2[4])

    return {
      kid: kid,
      payload: decodeCbor(cborPayload),
    }
  }

  async function verifyCose(message: string, jwk: object): Promise<boolean> {
    console.log(`Verifying: ${message} with ${JSON.stringify(jwk)}`)
    const messageBuffer = stringToBuffer(message)

    // cose-js library uses `require` etc. and doesn't seem to actually work in a browser for multiple reasons
    // @mattrglobal/cose might work but their licensing is not compatible with .. anything
    // might just have to submit this to a backend, maybe running Node, maybe running Python
    throw new Error("Cannot verify COSE yet")

    return true
  }
</script>

<main>
  <div id="reader" />
  {#if !scanning}
    <div class="controls">
      <button on:click={startScan}>Start scanning</button>
      <button on:click={scanPreset}>Simulate scan of preset data</button>
    </div>
  {/if}
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
    background: #ccc;
  }

  #reader {
    width: 100%;
    height: 100vh;
    min-height: 500px;
  }

  .controls {
    position: absolute;
    top: 16px;
    left: 16px;
    display: flex;
    flex-direction: row;
    gap: 16px;
  }

  button {
    padding: 32px;
    background-color: #fff;
    color: #000;
  }

  .scanner_borders {
    position: absolute;
    top: 20%;
    /* background-color: aliceblue; */
  }
</style>
