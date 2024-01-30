<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/CarbonFootprint_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/CarbonFootprint_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_CarbonFootprint_v0_1_DigitalProductPassport_Battery_CarbonFootprint_v0_1_post
     */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"

  type CarbonFootprint = {
    preProductionFootprint: number
    mainProductionFootprint: number
    referenceMaterial: string
  }

  export let data: {
    conformityDeclaration: string
    carbonFootprint: CarbonFootprint
  }
</script>

<article>
  {#if data.conformityDeclaration}
    <DataRow label="Conformity Declaration" link value={data.conformityDeclaration} />
  {/if}
  <div class="divider" />
  {#if data.carbonFootprint}
    <div class="title no-bottom-margin">Carbon Footprint</div>
    <div class="subtitle">
      The details of the carbon footprint for the battery production phases
    </div>
    <DataRow
      label="Pre Production Footprint"
      value={formatNumber(data.carbonFootprint.preProductionFootprint, "kg per kWh")}
    />
    <DataRow
      label="Main Production Footprint"
      value={formatNumber(data.carbonFootprint.mainProductionFootprint, "kg per kWh")}
    />
    <DataRow label="Reference Material" value={data.carbonFootprint.referenceMaterial} />
  {/if}
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
