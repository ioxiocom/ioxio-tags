<script lang="ts">
  import { decode as decodeCbor } from "cbor-x"
  import { BarcodeScanner } from "@capacitor-community/barcode-scanner"
  import { Buffer } from "buffer"
  import { decode as decodeBase45 } from "base45"
  import qrcode from "$assets/qrcode.png"
  import question from "$assets/question.svg"
  import logo from "$assets/logo.svg"
  import camera from "$assets/camera.svg"
  import subtract from "$assets/subtract.png"
  import Button from "$components/Button/index.svelte"
  import Loading from "$components/Loading/index.svelte"

  // Very uncool way of trying to fix the low quality library
  if (typeof window !== "undefined") {
    if (window.Buffer === undefined) {
      window.Buffer = Buffer
    }
  }

  const originalBodyBg = typeof document !== "undefined" ? document.body.style.background : ""

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

  function hideBackground() {
    BarcodeScanner.hideBackground()
    document.body.style.background = "transparent"
  }

  function showBackground() {
    BarcodeScanner.showBackground()
    document.body.style.background = originalBodyBg
  }

  function sleep(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms))
  }

  // TODO: On mobile devices where permissions allow for it, we should directly start scanning
  // TODO: https://github.com/capacitor-community/barcode-scanner#permissions for how to ask properly
  async function startScan() {
    const permissionResult = await BarcodeScanner.checkPermission({ force: true })
    if (!permissionResult.granted) {
      // Make a new permission request
      await navigator.mediaDevices.getUserMedia({ video: true })
      if (permissionResult.neverAsked) {
        return await startScan()
      } else {
        // TODO: Handle this somehow, e.g. show a screen asking to confirm permissions, depending on which result it is
        throw new Error(`Did not get camera permission, ${JSON.stringify(permissionResult)}`)
      }
    }

    scanning = true
    hideBackground()
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
        showBackground()
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

  async function tryParseIoxioTags(contents: string) {
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
          console.log("Parsed insecure data:", cborData)
          if (
            cborData.kid &&
            cborData.payload.iss &&
            cborData.payload.product &&
            cborData.payload.id
          ) {
            // This is an IOXIO Tags QR code
            console.log("IOXIO Tag detected, should continue to do more things")
            console.log(cborData.payload)

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
              verified = await verifyCose(b45decoded.toString(), jwk)
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
    const coseContainer = decodeCbor(message)
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
  <div id="reader">
    {#if !scanning}
      <div class="background" />
    {/if}
    <div class="relative barcode-scanner-area-wrapper">
      <div class="relative barcode-scanner-area">
        <img alt="subtract" class="subtract-image" src={subtract} />
        {#if scanning}
          <div class="square surround-cover" />
        {:else}
          <img class="logo" src={logo} alt="logo" />
        {/if}
      </div>
      <div class="relative">
        {#if scanning}
          <p class="description">Scan a Product Passport QR code to view product data</p>
        {:else}
          <p class="description">
            Turn on your camera for scan a Product Passport QR code to view product data
          </p>
        {/if}
      </div>
      {#if !scanning}
        <div class="relative button-wrapper">
          <Button onClick={startScan} icon={camera} title="Turn on" />
        </div>
      {/if}
    </div>
    {#if scanning}
      <div class="relative example-code-wrapper">
        <div class="example-description">
          Here's an example to identify an <strong>IOXIO Tag</strong>
        </div>
        <div class="example-code">
          <img src={qrcode} alt="code" />
        </div>
      </div>
    {/if}
    <a class="relative documentation-wrapper" href="/">
      <img alt="question" src={question} />
      <p class="documentation-label">Documentation</p>
    </a>
  </div>

  <div class="test">
    <div class="test-card">
      <div class="split">
        <div>
          <h2>Available Dataproduct name</h2>
          <span>Dataproduct description</span>
        </div>
        <div>
          <Button title="Fetch >" />
        </div>
      </div>
      <hr />
      <Loading type="light" />
    </div>
    <Loading type="dark" />
  </div>
</main>

<style lang="scss">
  .test {
    display: none; // This element just for testing, to be removed later
    position: absolute;
    z-index: 2123153;
    bottom: 5rem;
  }

  .test-card {
    .split {
      display: flex;
      flex-direction: row;
      gap: 2rem;
      align-items: end;
    }

    color: #fff;
    font-family: "Poppins", sans-serif;

    h2 {
      margin: 0;
    }

    hr {
      border-color: #20303e;
    }

    background: #1a2934;
    padding: 2rem;
    border-radius: 5px;
  }

  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
    background: transparent;
  }

  #reader {
    width: 100%;
    min-height: 500px;
    display: flex;
    flex-direction: column;
    padding: 1rem;
  }

  .relative {
    position: relative;
    z-index: 1;
  }

  .background {
    background: rgba(16, 25, 32, 1);
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
  }

  .barcode-scanner-area-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem;
    margin: auto;
  }

  .barcode-scanner-area {
    display: flex;
    justify-content: center;
    width: fit-content;
    margin-left: auto;
    margin-right: auto;
  }

  .subtract-image {
    position: relative;
    width: auto;
    z-index: 1;
    max-height: 40vh;
  }

  @media screen and (max-width: 520px) {
    .subtract-image {
      width: 100%;
    }
  }

  .surround-cover {
    box-shadow: 0 0 0 99999px rgba(16, 25, 32, 0.83);
  }

  .square {
    position: absolute;
    left: 0.5rem;
    top: 0.5rem;
    width: calc(100% - 1rem);
    height: calc(100% - 1rem);
    border-radius: 0.8rem;
  }

  .description {
    text-align: center;
    font-size: 1rem;
    color: white;
    margin-top: 3rem;
    font-family: "Poppins", sans-serif;
  }

  .example-code-wrapper {
    border-radius: 0.5rem;
    padding: 1rem;
    background: rgba(32, 48, 62, 1);
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 1rem;
  }

  .example-description {
    color: white;
    font-size: 1.1rem;
    flex: 1;
    font-family: "Poppins", sans-serif;
  }

  .example-code {
    padding: 0.5rem;
    background-color: white;
    border-radius: 0.5rem;
    max-width: 7rem;
    display: flex;
  }

  .example-code img {
    width: 100%;
  }

  .documentation-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 1rem;
    gap: 0.5rem;
  }

  .documentation-wrapper img {
    width: 2rem;
  }

  .documentation-label {
    color: white;
    font-size: 1.2rem;
    font-family: "Poppins", sans-serif;
  }

  .button-wrapper {
    display: flex;
    justify-content: center;
    margin-top: 2rem;
  }

  .logo {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
</style>
