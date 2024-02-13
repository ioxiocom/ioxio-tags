<script lang="ts">
  /*
      Docs:

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/MobileWorkMachine/EnvironmentalFootprint_v0.1

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/MobileWorkMachine/EnvironmentalFootprint_v0.1.py

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_MobileWorkMachine_EnvironmentalFootprint_v0_1_DigitalProductPassport_MobileWorkMachine_EnvironmentalFootprint_v0_1_post
       */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"

  export let data: {
    carbonFootprint: {
      mainProductionFootprint: number
      preProductionFootprint: number
      referenceMaterial: string
    }
    materialWaste: {
      amount: number
      referenceMaterial: string
    }
  }
</script>

<article>
  <div class="title no-bottom-margin">Carbon footprint</div>
  <div class="subtitle">Carbon footprint of a mobile work machine</div>
  <DataRow
    label="Pre production footprint"
    value={formatNumber(data.carbonFootprint.preProductionFootprint, "kg CO2e / kWh")}
  />
  <DataRow
    label="Main production footprint"
    value={formatNumber(data.carbonFootprint.mainProductionFootprint, "kg CO2e / kWh")}
  />
  <DataRow label="Reference material" link value={data.carbonFootprint.referenceMaterial} />
  <div class="divider" />
  <div class="title no-bottom-margin">Material waste</div>
  <div class="subtitle">The details of the material waste generated during the production</div>
  <DataRow label="Amount" value={formatNumber(data.materialWaste.amount, "kg")} />
  <DataRow label="Reference material" link value={data.materialWaste.referenceMaterial} />
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
