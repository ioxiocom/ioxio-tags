<script lang="ts">
  /*
        Docs:

        https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Product/GrainPassport_v0.1

        https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Product/GrainPassport_v0.1.py

        https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Product_GrainPassport_v0_1_DigitalProductPassport_Product_GrainPassport_v0_1_post
      */

  import { formatNumber, countryListAlpha3, localizeDate, localizeDateTime } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Divider from "$components/Divider/index.svelte"

  enum ProductionMethod {
    CONVENTIONAL = "Conventional",
    ORGANIC = "Organic",
    NON_GMO = "Non-GMO",
    REGENERATIVE = "Regenerative",
    IDENTITY_PRESERVED_GRAIN = "Identity-Preserved Grain",
    OTHER = "Other",
  }

  export let data: {
    grainPassportNumber: string
    creationDate: string
    grainType: string
    grainVariety: string
    harvestYear: number
    productionMethod: ProductionMethod
    recipientInformation: {
      company: string
      businessId: string
      address: string
      zipcode: string
      city: string
      country: string
      contractNumber: string
      receptionDate: string
      signature: string
    }[]
    farmerInformation: {
      farm: string
      businessId: string
      address: string
      zipcode: string
      city: string
      country: string
      processingEquipment: string[]
      treatedWithGlyphosate: boolean
      treatedWithGrowthRegulator: boolean
      growthRegulatorDetails: {
        growthRegulatorDate: string
        growthRegulatorType: string
      }[]
      signature: string
    }[]
    transportInformation: {
      company: string
      truckRegistrationNumber: string
      driver: string
      shipmentWeight: number
      loadingTime: string
      unloadingTime: string
      previousContent: string
      previousContentDate: string
      previousSanitation: string
    }[]
  }

  const { recipientInformation, farmerInformation, transportInformation } = data
</script>

<Article>
  <DataRow label="Grain passport number" value={data.grainPassportNumber} />
  <DataRow label="Creation date" value={localizeDate(data.creationDate)} />
  <DataRow label="Grain type" value={data.grainType} />
  <DataRow label="Grain variety" value={data.grainVariety} />
  <DataRow label="Harvest year" value={data.harvestYear.toString()} />
  <DataRow label="Production method" value={data.productionMethod} />
  <Divider />
  <SectionHeader title="Recipient information">
    Information about all the recipients of the bag.
  </SectionHeader>
  {#each recipientInformation as recipient, index}
    <DataRow label="Company" value={recipient.company} />
    <DataRow label="Business ID" value={recipient.businessId} />
    <DataRow label="Address" value={recipient.address} />
    <DataRow label="ZIP code" value={recipient.zipcode} />
    <DataRow label="City" value={recipient.city} />
    <DataRow label="Coutry" value={countryListAlpha3[recipient.country]} />
    <DataRow label="Contract number" value={recipient.contractNumber} />
    <DataRow label="Date received" value={localizeDate(recipient.receptionDate)} />
    <DataRow label="Signature" value={recipient.signature} />
    {#if index !== farmerInformation.length - 1}
      <div class="list-separator" />
    {/if}
  {/each}
  <Divider />
  <SectionHeader title="Farmer information">Information about the farmers.</SectionHeader>
  {#each farmerInformation as farmer, index}
    <DataRow label="Farm" value={farmer.farm} />
    <DataRow label="Business ID" value={farmer.businessId} />
    <DataRow label="Address" value={farmer.address} />
    <DataRow label="ZIP code" value={farmer.zipcode} />
    <DataRow label="City" value={farmer.city} />
    <DataRow label="Coutry" value={countryListAlpha3[farmer.country]} />
    <DataRow label="Processing equipment" value={farmer.processingEquipment} />
    <DataRow label="Treated with glyphosate" value={farmer.treatedWithGlyphosate} />
    <DataRow label="Treated with growth regulator" value={farmer.treatedWithGrowthRegulator} />
    <DataRow
      label="Growth regulator details"
      value={farmer.growthRegulatorDetails
        .sort(
          (a, b) =>
            new Date(b.growthRegulatorDate).getTime() - new Date(a.growthRegulatorDate).getTime()
        )
        .map((regulator) => {
          return `${localizeDate(regulator.growthRegulatorDate)}: ${regulator.growthRegulatorType}`
        })}
    />
    <DataRow label="Signature" value={farmer.signature} />
    {#if index !== farmerInformation.length - 1}
      <div class="list-separator" />
    {/if}
  {/each}
  <Divider />
  <SectionHeader title="Transport information">
    Information about the transporting parties.
  </SectionHeader>
  {#each transportInformation as transport, index}
    <DataRow label="Company" value={transport.company} />
    <DataRow label="Truck registration number" value={transport.truckRegistrationNumber} />
    <DataRow label="Driver" value={transport.driver} />
    <DataRow label="Shipment weight	" value={formatNumber(transport.shipmentWeight, "kg")} />
    <DataRow label="Loading time" value={localizeDateTime(transport.loadingTime)} />
    <DataRow label="Unloading time" value={localizeDateTime(transport.unloadingTime)} />
    <DataRow label="Previous content date" value={localizeDate(transport.previousContentDate)} />
    <DataRow label="Previous content" value={transport.previousContent} />
    <DataRow label="Previous sanitation" value={transport.previousSanitation} />
    {#if index !== farmerInformation.length - 1}
      <div class="list-separator" />
    {/if}
  {/each}
</Article>

<style lang="scss">
  @import "$styles/variables.scss";

  .list-separator {
    height: 1px;
    width: 30%;
    background-color: $color-primary-dark;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 1rem;
  }
</style>
