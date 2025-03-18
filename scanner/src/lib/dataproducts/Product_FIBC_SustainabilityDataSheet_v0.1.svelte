<script lang="ts">
  /*
    Docs:

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Product/FIBC/SustainabilityDataSheet_v0.1

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Product/FIBC/SustainabilityDataSheet_v0.1.py

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Product_FIBC_SustainabilityDataSheet_v0_1_DigitalProductPassport_Product_FIBC_SustainabilityDataSheet_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Divider from "$components/Divider/index.svelte"

  export let data: {
    carbonFootprint: number
    rawMaterialEmissions: {
      emissions: number
    }
    processingEmissions: {
      emissions: number
    }
    transportEmissions: {
      transportLength: number
      fuelType: string
      emissions: number
    }
    circularityRate: number
    isRecyclable: boolean
    recyclingInstructions: string
    reusePolicy: string
  }
  const { rawMaterialEmissions, processingEmissions, transportEmissions } = data
</script>

<Article>
  <DataRow label="Carbon footprint" value={formatNumber(data.carbonFootprint, "kg CO2e")} />
  <DataRow
    label="Raw material emissions"
    value={formatNumber(rawMaterialEmissions.emissions, "kg CO2e")}
  />
  <DataRow
    label="Processing emissions"
    value={formatNumber(processingEmissions.emissions, "kg CO2e")}
  />
  <Divider />
  <SectionHeader title="Transport emissions">
    <p>Details of the emissions from the transportation of the bag.</p>
  </SectionHeader>
  <DataRow
    label="Transport length"
    value={formatNumber(transportEmissions.transportLength, "km")}
  />
  <DataRow label="Fuel type" value={transportEmissions.fuelType} />
  <DataRow label="Emissions" value={formatNumber(transportEmissions.emissions, "kg CO2e")} />
  <Divider />
  <DataRow label="Circularity rate" value={formatNumber(data.circularityRate, "%")} />
  <DataRow label="Is recyclable" value={data.isRecyclable} />
  <DataRow label="Recycling instructions" value={data.recyclingInstructions} />
  <DataRow label="Reuse policy" value={data.reusePolicy} />
</Article>
