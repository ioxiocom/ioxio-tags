<script lang="ts">
  import { BarcodeScanner } from "@capacitor-community/barcode-scanner/src/index"
  import { consoleLog } from "$lib/common"
  import { tryParseIoxioTags, type Payload } from "$lib/parse"
  import Button from "$components/Button/index.svelte"

  import IoxioTagExample from "$assets/ioxio-tag-example.png"
  import Subtract from "$assets/subtract.svg"
  import Failed from "$assets/failed.svg"
  import { onDestroy, onMount } from "svelte"
  import Documentation from "$components/Documentation/index.svelte"
  import { goto } from "$app/navigation"

  let originalBodyBg: string
  let isScanning: boolean = true
  let scanResult: Payload

  function hideBackground() {
    BarcodeScanner.hideBackground()

    if (typeof document !== "undefined") {
      document.body.style.background = "transparent"
    }
  }

  function showBackground() {
    BarcodeScanner.showBackground()

    if (typeof document !== "undefined") {
      document.body.style.background = originalBodyBg
    }
  }

  function rescan() {
    isScanning = true
    startScan()
  }

  function showMetaData(verified = true) {
    // Go to MetaData screen
    goto(`/q/${scanResult.iss}/${scanResult.product}/${scanResult.id}?verified=${verified}`)
  }

  // TODO: On mobile devices where permissions allow for it, we should directly start scanning
  // TODO: https://github.com/capacitor-community/barcode-scanner#permissions for how to ask properly
  async function startScan(): Promise<void> {
    // TODO: Permissions cannot be ignored
    const permissionResult = await BarcodeScanner.checkPermission({ force: true })
    if (!permissionResult.granted) {
      // Make a new permission request
      await navigator.mediaDevices.getUserMedia({ video: true })
      if (permissionResult.neverAsked) {
        return await startScan()
      } else {
        // TODO: Handle this somehow, e.g. show a screen asking to confirm permissions, depending on which result it is
        consoleLog(`Did not get camera permission, ${JSON.stringify(permissionResult)}`, "warn")
        throw new Error(`Did not get camera permission, ${JSON.stringify(permissionResult)}`)
      }
    }

    hideBackground()
    const result = await BarcodeScanner.startScan() // start scanning and wait for a result

    // If the result has content
    if (result.hasContent) {
      const payload = await tryParseIoxioTags(result.content)

      if (payload) {
        consoleLog("Detected IOXIO Tag")

        // No more need to scan
        BarcodeScanner.stopScan().then(() => {})

        scanResult = payload

        if (scanResult.verified) {
          showMetaData()
        } else {
          showBackground()
          isScanning = false
        }
      } else {
        consoleLog("No IOXIO Tag detected", "warn")
        // TODO: This should just continue scanning
        showBackground()
      }
    }
  }

  onMount(() => {
    if (typeof document !== "undefined") {
      originalBodyBg = document.body.style.background
    }

    startScan()
  })

  onDestroy(() => {
    BarcodeScanner.stopScan()
    showBackground()
  })
</script>

{#if isScanning}
  <div class="relative barcode-scanner-area-wrapper">
    <div class="relative barcode-scanner-area">
      <img alt="subtract" class="subtract-image" src={Subtract} />
      <div class="square surround-cover" />
    </div>
    <div class="relative">
      <p class="description">Scan a Product Passport QR code to view product data</p>
    </div>
  </div>
  <div class="relative example-code-wrapper">
    <div class="example-description">
      Here's an example to identify an <strong>IOXIO Tag</strong>
    </div>
    <div class="example-code">
      <img alt="An example IOXIO Tag" src={IoxioTagExample} />
    </div>
  </div>
  <Documentation />
{:else}
  <div class="relative failed-verification-wrapper">
    <img src={Failed} alt="" aria-hidden="true" />
    <div>
      <p>Code failed authenticity verification</p>
      <p>Continue anyway?</p>
    </div>
  </div>
  <div class="actions-wrapper">
    <Button title="No" width="100%" onClick={rescan} />
    <Button title="Yes" background="#E47987" width="100%" onClick={() => showMetaData(false)} />
  </div>
{/if}

<style lang="scss">
  .barcode-scanner-area-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem;
    margin: auto;
    @media screen and (max-height: 600px) {
      padding: 0.5rem 0;
    }
  }
  .failed-verification-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 3.1875rem;
    margin: auto;
    @media screen and (max-height: 600px) {
      padding: 0.5rem 0;
    }
    img {
      width: 5rem;
      height: 5rem;
    }
    p {
      color: #eeefec;
      text-align: center;
      font-size: 1rem;
      font-style: normal;
      font-weight: 400;
      line-height: 150%; /* 24px */
    }
  }
  .actions-wrapper {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
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
    @media screen and (max-height: 600px) {
      max-height: 30vh;
    }
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
    @media screen and (max-height: 600px) {
      margin-top: 1rem;
      font-size: 0.8rem;
      line-height: 0.75rem;
    }
  }

  .example-code-wrapper {
    border-radius: 0.5rem;
    padding: 1rem;
    background: rgba(32, 48, 62, 1);
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 1rem;
    @media screen and (max-height: 600px) {
      padding: 0.5rem;
      margin-bottom: 0.5rem;
      gap: 0.5rem;
    }
  }

  .example-description {
    color: white;
    font-size: 1.1rem;
    flex: 1;
    @media screen and (max-height: 600px) {
      font-size: 0.7rem;
      line-height: 0.75rem;
    }
  }

  .example-code {
    padding: 0.5rem;
    background-color: white;
    border-radius: 0.5rem;
    max-width: 7rem;
    display: flex;
    @media screen and (max-height: 600px) {
      max-width: 3rem;
    }
  }

  .example-code img {
    width: 100%;
  }
</style>
