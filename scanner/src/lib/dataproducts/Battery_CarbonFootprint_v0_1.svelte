<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/CarbonFootprint_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/CarbonFootprint_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_CarbonFootprint_v0_1_DigitalProductPassport_Battery_CarbonFootprint_v0_1_post
     */

  import { countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Common/Divider/index.svelte"
  import Title from "$components/Common/Title/index.svelte"
  import SubTitle from "$components/Common/SubTitle/index.svelte"
  import Article from "$components/Common/Article/index.svelte"

  type CarbonFootprint = {
    preProductionFootprint: number
    mainProductionFootprint: number
    referenceMaterial: string
  }

  export let status: number
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
</script>

<Article>
  <DataRow label="Battery model" value={data.batteryModel} />
  <DataRow label="Conformity declaration" column link value={data.conformityDeclaration} />
  <Divider />
  <Title class="no-bottom-margin">Manufacturer information</Title>
  <SubTitle>The details of the battery manufacturer</SubTitle>
  <DataRow label="Name" value={data.manufacturerInformation?.name} />
  <DataRow label="Street name" value={data.manufacturerInformation?.streetName} />
  <DataRow label="Postal code" value={data.manufacturerInformation?.postalCode} />
  <DataRow label="City" value={data.manufacturerInformation?.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturerInformation?.country]} />
  <DataRow label="Website" link column value={data.manufacturerInformation?.website} />
  <DataRow label="Email" column value={data.manufacturerInformation?.email} />
  <Divider />
  <Title class="no-bottom-margin">Manufacturing location</Title>
  <SubTitle>The details of the location of the battery manufacturing plant</SubTitle>
  <DataRow label="City" value={data.manufacturingLocation?.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturingLocation?.country]} />
  <Divider />
  <Title class="no-bottom-margin">Carbon footprint</Title>
  <SubTitle>The details of the carbon footprint for the battery production phases</SubTitle>
  <DataRow
    label="Pre-production footprint"
    value={formatNumber(data.carbonFootprint?.preProductionFootprint, "kg CO2e / kWh")}
  />
  <DataRow
    label="Main production footprint"
    value={formatNumber(data.carbonFootprint?.mainProductionFootprint, "kg CO2e / kWh")}
  />
  <DataRow label="Reference material" column link value={data.carbonFootprint?.referenceMaterial} />
</Article>
