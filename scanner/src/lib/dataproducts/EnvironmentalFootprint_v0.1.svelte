<script lang="ts">
  /*
    Docs:

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/EnvironmentalFootprint_v0.1

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/EnvironmentalFootprint_v0.1.py

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_EnvironmentalFootprint_v0_1_DigitalProductPassport_EnvironmentalFootprint_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Divider from "$components/Divider/index.svelte"

  export let data: {
    carbonFootprint: {
      rawMaterialFootprint: number
      componentProductionFootprint: number
      mainProductionFootprint: number
      transportationFootprint: number
      referenceMaterial: string
    }
    materialWaste: {
      amount: number
      referenceMaterial: string
    }
  }
  const footprint = data.carbonFootprint
  const waste = data.materialWaste
</script>

<Article>
  <SectionHeader title="Carbon footprint">
    <p>The details of the carbon footprint during production.</p>
  </SectionHeader>
  <DataRow
    label="Raw material footprint"
    value={formatNumber(footprint.rawMaterialFootprint, "CO2e")}
  />
  <DataRow
    label="Component production footprint"
    value={formatNumber(footprint.componentProductionFootprint, "CO2e")}
  />
  <DataRow
    label="Main production footprint"
    value={formatNumber(footprint.mainProductionFootprint, "CO2e")}
  />
  <DataRow
    label="Transportation footprint"
    value={formatNumber(footprint.transportationFootprint, "CO2e")}
  />
  <DataRow label="Reference material" value={footprint.referenceMaterial} />
  <Divider />
  <SectionHeader title="Material waste">
    <p>Details of the material waste generated during production.</p>
  </SectionHeader>
  <DataRow label="Amount" value={formatNumber(waste.amount, "kg")} />
  <DataRow label="Reference material" value={waste.referenceMaterial} />
</Article>

<style lang="scss">
  p {
    margin: 0.5rem 0;
  }
</style>
