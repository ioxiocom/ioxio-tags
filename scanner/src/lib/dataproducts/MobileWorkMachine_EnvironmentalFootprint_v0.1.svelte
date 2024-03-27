<script lang="ts">
  /*
      Docs:

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/MobileWorkMachine/EnvironmentalFootprint_v0.1

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/MobileWorkMachine/EnvironmentalFootprint_v0.1.py

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_MobileWorkMachine_EnvironmentalFootprint_v0_1_DigitalProductPassport_MobileWorkMachine_EnvironmentalFootprint_v0_1_post
       */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"

  export let status: number
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

<Article>
  <SectionHeader title="Carbon footprint">Carbon footprint of a mobile work machine</SectionHeader>
  <DataRow
    label="Pre-production footprint"
    value={formatNumber(data.carbonFootprint.preProductionFootprint, "kg CO2e / kWh")}
  />
  <DataRow
    label="Main production footprint"
    value={formatNumber(data.carbonFootprint.mainProductionFootprint, "kg CO2e / kWh")}
  />
  <DataRow label="Reference material" column link value={data.carbonFootprint.referenceMaterial} />
  <Divider />
  <SectionHeader title="Material waste">
    The details of the material waste generated during the production
  </SectionHeader>
  {#if data.materialWaste}
    <DataRow label="Amount" value={formatNumber(data.materialWaste.amount, "kg")} />
    <DataRow label="Reference material" link value={data.materialWaste.referenceMaterial} />
  {:else}
    <span>-</span>
  {/if}
</Article>
