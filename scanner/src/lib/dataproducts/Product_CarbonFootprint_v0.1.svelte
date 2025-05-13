<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/Product/CarbonFootprint_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/Product/CarbonFootprint_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/Product_CarbonFootprint_v0_1_Product_CarbonFootprint_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"

  export let data: {
    logisticsFootprint: number
    materialFootprint: number
    processingFootprint: number
  }

  const totalFootprint = data.logisticsFootprint + data.materialFootprint + data.processingFootprint
</script>

<Article>
  <SectionHeader title="Carbon Footprint">
    Breakdown of the product's carbon footprint by category (kg CO₂e)
  </SectionHeader>

  <DataRow label="Total carbon footprint" value={formatNumber(totalFootprint, "kg CO₂e")} />

  <Divider />

  <DataRow label="Material footprint" value={formatNumber(data.materialFootprint, "kg CO₂e")} />
  <DataRow label="Processing footprint" value={formatNumber(data.processingFootprint, "kg CO₂e")} />
  <DataRow label="Logistics footprint" value={formatNumber(data.logisticsFootprint, "kg CO₂e")} />
</Article>
