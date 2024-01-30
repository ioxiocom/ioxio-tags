<script lang="ts">
  /*
      Docs:

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.1.py

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.1

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_MobileWorkMachine_Drill_ManufacturingDataSheet_v0_1_DigitalProductPassport_MobileWorkMachine_Drill_ManufacturingDataSheet_v0_1_post
       */

  import { camelCaseToWords, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"

  export let data: {
    productName: string
    boomCoverage: number
    trammingDistance: number
    maximumHoleLength: number
    minimumHoleDiameter: number
    maximumHoleDiameter: number
    drillingPower: number
    safetyDataSheet: string
    manufacturerInformation: {
      name: string
      streetName: string
      postalCode: string
      city: string
      country: string
      website: string
      email: string
    }
  }
</script>

<article>
  <DataRow label="Product Name" value={data.productName} />
  <DataRow label="Boom Coverage" value={formatNumber(data.boomCoverage, "m")} />
  <DataRow label="Tramming Distance" value={formatNumber(data.trammingDistance, "km")} />
  <DataRow label="Maximum Hole Length" value={formatNumber(data.maximumHoleLength, "m")} />
  <DataRow label="Minimum Hole Diameter" value={formatNumber(data.minimumHoleDiameter, "mm")} />
  <DataRow label="Maximum Hole Diameter" value={formatNumber(data.maximumHoleDiameter, "mm")} />
  <DataRow label="Drilling Power" value={formatNumber(data.drillingPower, "kW")} />
  <DataRow label="Safety Data Sheet" link value={data.safetyDataSheet} />
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturer Information</div>
  <div class="subtitle">The details of the drill manufacturer</div>
  {#each Object.entries(data.manufacturerInformation) as [key, value]}
    <DataRow label={camelCaseToWords(key)} {value} />
  {/each}
</article>

<style lang="scss">
  article {
    color: white;
    font-style: normal;
    .title {
      font-size: 1rem;
      font-weight: 500;
      line-height: 1.5rem;
      margin-bottom: 1rem;
      &.no-bottom-margin {
        margin-bottom: 0;
      }
    }
    .subtitle {
      font-size: 0.75rem;
      font-weight: 400;
      color: white;
      margin-bottom: 1rem;
    }
    .divider {
      padding-bottom: 1rem;
      border-bottom: 1px solid #20303e;
      margin-bottom: 1rem;
    }
  }
</style>
