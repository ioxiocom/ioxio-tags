<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/CarbonFootprint_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/CarbonFootprint_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_CarbonFootprint_v0_1_DigitalProductPassport_Battery_CarbonFootprint_v0_1_post
     */

  import { countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import EmissionsPieChart from "$assets/battery-emissions-chart.svg?raw"
  import FootprintPieChart from "$assets/battery-carbon-footprint-chart.svg?raw"
  import { inview } from "svelte-inview"

  type CarbonFootprint = {
    preProductionFootprint: number
    mainProductionFootprint: number
    referenceMaterial: string
  }

  export let status: number
  export let id: string
  export let data: {
    batteryModel: string
    conformityDeclaration: string
    manufacturerInformation: {
      name: string
      streetName: string
      postalCode: string
      city: string
      country: string
      website: string
      email: string
    }
    manufacturingLocation: {
      city: string
      country: string
    }
    carbonFootprint: CarbonFootprint
  }

  const minexpoDemo = id === "minexpo-demo-1"
  let animateFirstChart = false
  let animateSecondChart = false
  let animationDelay = 500
</script>

<Article>
  <DataRow label="Battery model" value={data.batteryModel} />
  <DataRow label="Conformity declaration" column link value={data.conformityDeclaration} />
  <Divider />
  {#if minexpoDemo}
    <SectionHeader title="Battery carbon footprint" />
    <div class="description">
      Carbon footprint of a battery as required by the European Commission’s Battery Act
      (2023/1542).
      <span class="asterisk">1</span>
    </div>
    <div
      class="chart-wrapper"
      class:animate-second={animateSecondChart}
      use:inview={{}}
      on:inview_enter={() => {
        setTimeout(() => {
          animateSecondChart = true
        }, animationDelay)
      }}
      on:inview_leave={() => {
        animateSecondChart = false
      }}
    >
      {@html FootprintPieChart}
      <div>
        <p>
          Battery carbon footprint includes emissions of cells, transportation and other activities.
        </p>
        <p>
          Please contact your Sandvik representative for detailed information for your exact
          product.
        </p>
      </div>
    </div>
    <Divider />
    <SectionHeader title="Lifecycle emissions of a machine ²" />
    <div
      class="chart-wrapper"
      class:animate={animateFirstChart}
      use:inview={{}}
      on:inview_enter={() => {
        setTimeout(() => {
          animateFirstChart = true
        }, animationDelay)
      }}
      on:inview_leave={() => {
        animateFirstChart = false
      }}
    >
      {@html EmissionsPieChart}
      <p>
        Sandvik performs validated product-specific emission calculations based on generic emission
        calculation approaches.
        <span class="asterisk">3</span>
      </p>
    </div>
    <Divider />
    <div class="description">
      <div>1. Depends on the country under consideration. Figures are examples.</div>
      <div>2. GHG Protocol, ISO 14000 series. Product category rules (PCR).</div>
      <div>3. Digital Battery Passport meets the new EU Battery regulation requirements.</div>
    </div>
  {:else}
    <SectionHeader title="Manufacturer information">
      The details of the battery manufacturer
    </SectionHeader>
    <DataRow label="Name" value={data.manufacturerInformation?.name} />
    <DataRow label="Street name" value={data.manufacturerInformation?.streetName} />
    <DataRow label="Postal code" value={data.manufacturerInformation?.postalCode} />
    <DataRow label="City" value={data.manufacturerInformation?.city} />
    <DataRow label="Country" value={countryListAlpha3[data.manufacturerInformation?.country]} />
    <DataRow label="Website" link column value={data.manufacturerInformation?.website} />
    <DataRow label="Email" column value={data.manufacturerInformation?.email} />
    <Divider />
    <SectionHeader title="Manufacturing location">
      The details of the location of the battery manufacturing plant
    </SectionHeader>
    <DataRow label="City" value={data.manufacturingLocation?.city} />
    <DataRow label="Country" value={countryListAlpha3[data.manufacturingLocation?.country]} />
    <Divider />
    <SectionHeader title="Carbon footprint">
      The details of the carbon footprint for the battery production phases
    </SectionHeader>
    <DataRow
      label="Pre-production footprint"
      value={formatNumber(data.carbonFootprint?.preProductionFootprint, "kg CO2e / kWh")}
    />
    <DataRow
      label="Main production footprint"
      value={formatNumber(data.carbonFootprint?.mainProductionFootprint, "kg CO2e / kWh")}
    />
    <DataRow
      label="Reference material"
      column
      link
      value={data.carbonFootprint?.referenceMaterial}
    />
  {/if}
</Article>

<style lang="scss">
  .description {
    position: relative;
    font-size: 0.75rem;
  }

  .asterisk {
    font-size: 0.5rem;
    position: absolute;
    transform: translate(2px, 0px);
  }

  .chart-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 1rem;

    p {
      font-size: 0.75rem;
    }

    :global(svg) {
      max-width: 25rem;
      margin: 0 auto;
    }
  }

  $animation-speed: 650ms;

  :global(.chart-wrapper.animate svg #slice-0) {
    animation: scale0 $animation-speed ease-in-out;

    @keyframes scale0 {
      50%,
      100% {
        transform: scale(1);
        transform-origin: center;
      }
      75% {
        transform: scale(1.02);
        transform-origin: center;
      }
    }
  }

  :global(.chart-wrapper.animate svg #slice-1) {
    animation: scale1 $animation-speed ease-in-out;

    @keyframes scale1 {
      0%,
      50%,
      100% {
        transform: scale(1);
        transform-origin: center;
      }
      25% {
        transform: scale(1.04);
        transform-origin: center;
      }
    }
  }

  :global(.chart-wrapper.animate svg #slice-2) {
    animation: scale2 $animation-speed ease-in-out;

    @keyframes scale2 {
      10%,
      60%,
      100% {
        transform: scale(1);
        transform-origin: center;
      }
      35% {
        transform: scale(1.04);
        transform-origin: center;
      }
    }
  }

  :global(.chart-wrapper.animate svg #slice-3) {
    animation: scale3 $animation-speed ease-in-out;

    @keyframes scale3 {
      20%,
      70%,
      100% {
        transform: scale(1);
        transform-origin: center;
      }
      45% {
        transform: scale(1.04);
        transform-origin: center;
      }
    }
  }

  :global(.chart-wrapper.animate svg #slice-4) {
    animation: scale4 $animation-speed ease-in-out;

    @keyframes scale4 {
      30%,
      80%,
      100% {
        transform: scale(1);
        transform-origin: center;
      }
      55% {
        transform: scale(1.04);
        transform-origin: center;
      }
    }
  }

  :global(.chart-wrapper.animate-second svg #slice-0) {
    animation: scale00 $animation-speed ease-in-out;

    @keyframes scale00 {
      0%,
      50%,
      100% {
        transform: scale(1);
        transform-origin: center;
      }
      25% {
        transform: scale(1.04);
        transform-origin: center;
      }
    }
  }

  :global(.chart-wrapper.animate-second svg #slice-1) {
    animation: scale01 $animation-speed ease-in-out;

    @keyframes scale01 {
      10%,
      60%,
      100% {
        transform: scale(1);
        transform-origin: center;
      }
      35% {
        transform: scale(1.04);
        transform-origin: center;
      }
    }
  }

  :global(.chart-wrapper.animate-second svg #slice-2) {
    animation: scale02 $animation-speed ease-in-out;

    @keyframes scale02 {
      20%,
      70%,
      100% {
        transform: scale(1);
        transform-origin: center;
      }
      45% {
        transform: scale(1.02);
        transform-origin: center;
      }
    }
  }
</style>
