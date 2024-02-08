<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/CarbonFootprint_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/CarbonFootprint_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_CarbonFootprint_v0_1_DigitalProductPassport_Battery_CarbonFootprint_v0_1_post
     */

  import { camelCaseToWords, countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"

  type CarbonFootprint = {
    preProductionFootprint: number
    mainProductionFootprint: number
    referenceMaterial: string
  }

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
  data.manufacturerInformation.country = countryListAlpha3[data.manufacturerInformation.country]
  data.manufacturingLocation.country = countryListAlpha3[data.manufacturingLocation.country]
</script>

<article>
  <DataRow label="Battery model" value={data.batteryModel} />
  {#if data.conformityDeclaration}
    <DataRow label="Conformity Declaration" link value={data.conformityDeclaration} />
  {/if}
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturer information</div>
  <div class="subtitle">The details of the battery manufacturer</div>
  {#each Object.entries(data.manufacturerInformation) as [key, value]}
    <DataRow label={camelCaseToWords(key)} {value} />
  {/each}
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturing location</div>
  <div class="subtitle">The details of the location of the battery manufacturing plant</div>
  {#each Object.entries(data.manufacturingLocation) as [key, value]}
    <DataRow label={camelCaseToWords(key)} {value} />
  {/each}
  {#if data.carbonFootprint}
    <div class="divider" />
    <div class="title no-bottom-margin">Carbon footprint</div>
    <div class="subtitle">
      The details of the carbon footprint for the battery production phases
    </div>
    <DataRow
      label="Pre production footprint"
      value={formatNumber(data.carbonFootprint.preProductionFootprint, "kg per kWh")}
    />
    <DataRow
      label="Main production footprint"
      value={formatNumber(data.carbonFootprint.mainProductionFootprint, "kg per kWh")}
    />
    <DataRow label="Reference material" value={data.carbonFootprint.referenceMaterial} />
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
