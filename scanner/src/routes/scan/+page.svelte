<script lang="ts">
  import { BarcodeScanner } from "@capacitor-community/barcode-scanner/src/index"
  import { goto } from "$app/navigation"
  import { App } from "@capacitor/app"
  import { consoleLog } from "$lib/common"
  import { tryParseIoxioTags, type Payload } from "$lib/parse"
  import Button from "$components/Button/index.svelte"

  import IoxioTagExample from "$assets/ioxio-tag-example.png"
  import Subtract from "$assets/subtract.svg"
  import FailedSvg from "$assets/failed.svg"
  import ErrorSvg from "$assets/error.svg"
  import { onDestroy, onMount } from "svelte"
  import Documentation from "$components/Documentation/index.svelte"

  const Status = {
    SCANNING: "SCANNING",
    SCAN_SUCCESS_VERIFIED: "SCAN_SUCCESS_VERIFIED",
    SCAN_SUCCESS_NOT_VERIFIED: "SCAN_SUCCESS_NOT_VERIFIED",
    SCAN_FAILED: "SCAN_FAILED",
  } as const

  type Status = typeof Status[keyof typeof Status]

  let noPermission = true
  let originalBodyBg: string
  let status: Status
  let scanResult: Payload

  function hideBackground() {
    if (typeof document !== "undefined") {
      BarcodeScanner.hideBackground()
      document.body.style.background = "transparent"
    }
  }

  function showBackground() {
    if (typeof document !== "undefined") {
      BarcodeScanner.showBackground()
      document.body.style.background = originalBodyBg
    }
  }

  function rescan() {
    startScan()
  }

  function showMetaData(verified = true) {
    // Go to MetaData screen
    let url = `/q/${scanResult.iss}/${scanResult.product}/${scanResult.id}?verified=${verified}`
    goto(url)
  }

  // TODO: On mobile devices where permissions allow for it, we should directly start scanning
  // TODO: https://github.com/capacitor-community/barcode-scanner#permissions for how to ask properly
  async function startScan(): Promise<void> {
    status = Status.SCANNING
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
        // No more need to scan
        BarcodeScanner.stopScan().then(() => {})

        scanResult = payload

        if (scanResult.verified) {
          showMetaData()
          status = Status.SCAN_SUCCESS_VERIFIED
        } else {
          showBackground()
          status = Status.SCAN_SUCCESS_NOT_VERIFIED
        }
      } else {
        consoleLog("No IOXIO Tag detected", "warn")
        // TODO: This should just continue scanning
        showBackground()
        status = Status.SCAN_FAILED
      }
    }
  }

  async function checkPermission() {
    const permissionResult = await BarcodeScanner.checkPermission()
    return !!permissionResult.granted
  }

  async function givePermission() {
    // checkPermission seems unreliable, getUserMedia might work better?
    await navigator.mediaDevices.getUserMedia({ video: true })
    const permissionResult = await BarcodeScanner.checkPermission({ force: true })
    if (!!permissionResult.granted) {
      noPermission = false
      startScan()
    }
  }

  onMount(async () => {
    if (typeof document !== "undefined") {
      originalBodyBg = document.body.style.background
      App.addListener("backButton", function (e) {
        App.exitApp()
      })
      if (await checkPermission()) {
        noPermission = false
        startScan()
      }
    }

    // Permission detection logic can't detect if autoplay is blocked
    window.onunhandledrejection = function _handleRejection(event) {
      const reasonText = String(event.reason)
      const scanErrors = ["NotAllowedError", "play() can only be initiated by a user gesture"]
      for (let scanError of scanErrors) {
        if (reasonText.includes(scanError)) {
          goto("/")
          break
        }
      }
    }
  })

  onDestroy(() => {
    BarcodeScanner.stopScan()
    showBackground()

    if (typeof window !== "undefined") {
      window.onunhandledrejection = () => {}
    }
  })
</script>

{#if noPermission}
  <div class="relative failed-verification-wrapper">
    <img src={ErrorSvg} alt="" aria-hidden="true" />
    <div>
      <p>We need camera permissions</p>
    </div>
  </div>
  <div class="actions-wrapper">
    <Button
      title="Give camera permissions"
      maxWidth="17rem"
      width="100%"
      height="3.125rem"
      onClick={givePermission}
    />
  </div>
{:else if status === Status.SCANNING || status === Status.SCAN_SUCCESS_VERIFIED}
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
{:else if status === Status.SCAN_SUCCESS_NOT_VERIFIED}
  <div class="relative failed-verification-wrapper">
    <img src={FailedSvg} alt="" aria-hidden="true" />
    <div>
      <p>Code failed authenticity verification</p>
      <p>{scanResult.error}</p>
      <p>Continue anyway?</p>
    </div>
  </div>
  <div class="actions-wrapper">
    <Button title="No" width="100%" height="3.125rem" onClick={rescan} />
    <Button
      title="Yes"
      background="#E47987"
      width="100%"
      height="3.125rem"
      onClick={() => showMetaData(false)}
    />
  </div>
{:else if status === Status.SCAN_FAILED}
  <div class="relative failed-verification-wrapper">
    <img src={ErrorSvg} alt="" aria-hidden="true" />
    <div>
      <p>Code is not recognized.</p>
      <p>Please try again or use another code</p>
    </div>
  </div>
  <div class="actions-wrapper">
    <Button title="Scan again" width="100%" height="3.125rem" onClick={rescan} />
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
    margin-bottom: 0.875rem;
    @media screen and (min-width: 36rem) {
      max-width: 33rem;
      width: 100%;
      margin: auto;
    }
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
