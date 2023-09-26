<script lang="ts">
  import IoxioTagLogo from "$assets/ioxio-tag-logo.svg"
  import Camera from "$assets/camera.svg"
  import Subtract from "$assets/subtract.svg"
  import Button from "$components/Button/index.svelte"
  import { goto } from "$app/navigation"
  import { consoleLog } from "$lib/common"
  import { tryParseIoxioTags } from "$lib/parse"
  import type { PageData } from "./$types"
  import Loading from "$components/Loading/index.svelte"

  export let data: PageData

  // Pregenerated data for testing
  const PRESET_DATA =
    "IT1:RRQ5 8/60V500GKOG8WA6CADOPCZQE..E6$CPQEGPCKI91/DXPE6$CSED -DUPCH$DV9EV3E $EQWEI93IEC7WEALE4W5" +
    "646D4FPX54%E5$CQX56%E:JC%JCPVC:P4WZCK-CM.CCA7H*6RW67W5VF6CA7XJC3UCAX57079460DCZX61:6256V50PEHZRA9A81+NMXJ0C76BJ" +
    "SUC**B1.VDCMQCKU47AZM52UW1K21R0VB6R55F2CXB/94+SS KBY92RZMO313+P1-O44PFWFB3BYELI.BHAW%2V2*4-AEGB0GX628CCJS1OBAU0" +
    "NH800JDD7UYPH+UNWL1KMH:UMAS4QK:R7$.36QVO8S5YA6SRW1LFA90H7.177ZM7QQ%HVZ 0VHLJQR%VLIPU/NJO68HZNA4PA32K9153Q8EW/%P" +
    "EKBRBNJO3ATK1WEW+P-PL.R0%MQJVTL68+FMLOFRAJ0IHR6W882.8B:EBEG24X74H9COJ:.1C89WFCL M+.C1XJ$Z3PM5OM754GL22D7TVXV*JH" +
    "/X1U66+CHCEMXI0P274GSM.6. LBDD"

  async function scanPreset() {
    const detected = await tryParseIoxioTags(PRESET_DATA)
    if (detected) {
      consoleLog("Detected IOXIO Tag")
    } else {
      consoleLog("No IOXIO Tag detected", "warn")
    }
  }
</script>

<div class="container">
  <div class="background" />
  <div class="relative barcode-scanner-area-wrapper">
    <div class="relative barcode-scanner-area">
      <img alt="subtract" class="subtract-image" src={Subtract} />
      <img class="logo" src={IoxioTagLogo} alt="logo" />
    </div>
    <div>
      <div class="relative">
        <p class="description">
          Turn on your camera for scan a Product Passport QR code to view product data
        </p>
      </div>
      <div class="relative actions-wrapper">
        <div>
          <Button onClick={() => goto("/scan")} icon={Camera} title="Turn on" />
        </div>
        {#if data.isDevelopment}
          <div>
            <Button onClick={scanPreset} title="Simulate scan of preset data" />
          </div>
        {/if}
      </div>
    </div>
  </div>
  <div class="test">
    <div class="test-card">
      <div class="split">
        <div>
          <h2>Available Dataproduct name</h2>
          <span>Dataproduct description</span>
        </div>
        <div>
          <Button title="Fetch >" onClick={() => {}} />
        </div>
      </div>
      <hr />
      <Loading type="light" />
    </div>
    <Loading type="dark" />
  </div>
</div>

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
    height: 100%;
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
  .description {
    text-align: center;
    font-size: 1rem;
    color: white;
    margin-top: 3rem;
  }
  .actions-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
  }
  .logo {
    width: 80%;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
</style>
