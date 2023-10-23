<script lang="ts">
  import IoxioTagLogo from "$assets/ioxio-tag-logo.svg"
  import Camera from "$assets/camera.svg"
  import Subtract from "$assets/subtract.svg"
  import Button from "$components/Button/index.svelte"
  import { goto } from "$app/navigation"
  import { consoleLog } from "$lib/common"
  import { tryParseIoxioTags } from "$lib/parse"
  import type { PageData } from "./$types"
  import Documentation from "$components/Documentation/index.svelte"

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
    const payload = await tryParseIoxioTags(PRESET_DATA)
    if (payload) {
      consoleLog("Detected IOXIO Tag")
      goto(`/q/${payload.iss}/${payload.product}/${payload.id}`)
    } else {
      consoleLog("No IOXIO Tag detected", "warn")
    }
  }
</script>

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
        <Button width="9rem" onClick={() => goto("/scan")} icon={Camera} title="Turn on" />
      </div>
      {#if data.isDevelopment}
        <div>
          <Button width="100%" onClick={scanPreset} title="Simulate scan of preset data" />
        </div>
      {/if}
    </div>
  </div>
</div>
<Documentation />

<style lang="scss">
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

  .barcode-scanner-area-wrapper {
    flex: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem;
    margin: auto;
    @media screen and (max-height: 600px) {
      justify-content: space-around;
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
  .actions-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
    @media screen and (max-height: 600px) {
      margin-top: 1rem;
    }
  }
  .logo {
    width: 80%;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
</style>
