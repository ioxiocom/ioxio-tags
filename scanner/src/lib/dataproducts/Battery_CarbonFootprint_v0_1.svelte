<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/CarbonFootprint_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/CarbonFootprint_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_CarbonFootprint_v0_1_DigitalProductPassport_Battery_CarbonFootprint_v0_1_post
     */

  import { countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"

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

<article>
  <DataRow label="Battery model" value={data.batteryModel} />
  <DataRow label="Conformity declaration" column link value={data.conformityDeclaration} />
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturer information</div>
  <div class="subtitle">The details of the battery manufacturer</div>
  <DataRow label="Name" value={data.manufacturerInformation.name} />
  <DataRow label="Street name" value={data.manufacturerInformation.streetName} />
  <DataRow label="Postal code" value={data.manufacturerInformation.postalCode} />
  <DataRow label="City" value={data.manufacturerInformation.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturerInformation.country]} />
  <DataRow label="Website" link column value={data.manufacturerInformation.website} />
  <DataRow label="Email" column value={data.manufacturerInformation.email} />
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturing location</div>
  <div class="subtitle">The details of the location of the battery manufacturing plant</div>
  <DataRow label="City" value={data.manufacturingLocation.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturingLocation.country]} />
  <div class="divider" />
  <div class="title no-bottom-margin">Carbon footprint</div>
  <div class="subtitle">The details of the carbon footprint for the battery production phases</div>
  <DataRow
    label="Pre-production footprint"
    value={formatNumber(data.carbonFootprint.preProductionFootprint, "kg CO2e / kWh")}
  />
  <DataRow
    label="Main production footprint"
    value={formatNumber(data.carbonFootprint.mainProductionFootprint, "kg CO2e / kWh")}
  />
  <DataRow label="Reference material" column link value={data.carbonFootprint.referenceMaterial} />
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
      border-bottom: 1px solid #20303e;
      margin-bottom: 1rem;
    }
  }
</style>
