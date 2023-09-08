<script lang="ts">
  import { decode as decodeCbor } from "cbor-x"
  // import { verify as verifyCose } from "@mattrglobal/cose"
  import { BarcodeScanner } from "@capacitor-community/barcode-scanner"
  import { Buffer } from "buffer"

  let scanning = false

  async function startScan() {
    // Check camera permission
    // This is just a simple example, check out the better checks below
    await BarcodeScanner.checkPermission({ force: true })

    // make background of WebView transparent
    // note: if you are using ionic this might not be enough, check below
    BarcodeScanner.hideBackground()

    const result = await BarcodeScanner.startScan() // start scanning and wait for a result

    // if the result has content
    if (result.hasContent) {
      console.log(result)
      await onScanSuccess(result.content)
      scanning = false
    }
  }

  function isTagsURL(url: string) {
    const urlPattern = /https:\/\/tags\.ioxio\.(dev|io)\/.*$/
    return urlPattern.test(url)
  }

  async function onScanSuccess(contents: string) {
    const isValidURL = isTagsURL(contents)
    if (isValidURL) {
      console.log("URL is valid for tags.ioxio.dev.")
      alert(`Code matched = ${contents}`)
    } else {
      console.log("URL is not valid for tags.ioxio.dev, maybe it's cbor?")
      const cborData = await parseCose(contents)
      console.log(cborData)
    }
  }

  function stringToBuffer(value: string): Buffer {
    return Buffer.from(value)
  }

  async function parseCose(message: string) {
    // TODO: Find a new COSE library that works
    const messageBuffer = stringToBuffer(message)
    const fakeVerifier = async function (a, b) {
      return true
    }

    return await verifyCose({
      payload: messageBuffer,
      verifier: {
        externalVerifier: fakeVerifier, // Used to skip signature verification at this stage
      },
    })
  }
</script>

<main>
  <div id="reader" />
  {#if !scanning}
    <button on:click={startScan}>Start scanning</button>
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

  button {
    position: absolute;
    top: 16px;
    left: 16px;
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
