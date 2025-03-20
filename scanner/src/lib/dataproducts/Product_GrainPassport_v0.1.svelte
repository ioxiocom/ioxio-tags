<script lang="ts">
  /*
        Docs:

        https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Product/GrainPassport_v0.1

        https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Product/GrainPassport_v0.1.py

        https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Product_GrainPassport_v0_1_DigitalProductPassport_Product_GrainPassport_v0_1_post
      */

  import {
    formatNumber,
    countryListAlpha3,
    makeHeader,
    localizeDate,
    localizeDateTime,
  } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Divider from "$components/Divider/index.svelte"

  import TrueIcon from "$assets/true-circle.svg"
  import FalseIcon from "$assets/false-circle.svg"

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
  <table>
    <tbody>
      <!-- Loop through the keys of the first object for headers in the left column -->
      {#each Object.keys(recipientInformation[0]) as header}
        <tr>
          {#if header === "businessId"}
            <th>Business ID</th>
          {:else if header === "zipcode"}
            <th>ZIP code</th>
          {:else if header === "receptionDate"}
            <th>Date received</th>
          {:else}
            <th>
              {makeHeader(header)}
            </th>
          {/if}
          <!-- Loop through each recipient and display the corresponding value for each header -->
          {#each recipientInformation as recipient}
            {#if header === "country"}
              <td>{countryListAlpha3[recipient[header]]}</td>
            {:else if header === "receptionDate"}
              <td>{localizeDate(recipient[header])}</td>
            {:else}
              <td>{recipient[header]}</td>
            {/if}
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
  <Divider />
  <SectionHeader title="Farmer information">Information about the farmers.</SectionHeader>
  <table>
    <tbody>
      {#each Object.keys(farmerInformation[0]) as header}
        <tr>
          {#if header === "businessId"}
            <th>Business ID</th>
          {:else if header === "zipcode"}
            <th>ZIP code</th>
          {:else}
            <th>
              {makeHeader(header)}
            </th>
          {/if}
          {#each farmerInformation as farmer}
            {#if header === "country"}
              <td>{countryListAlpha3[farmer[header]]}</td>
            {:else if typeof farmer[header] === "boolean"}
              <td>
                <img
                  src={farmer[header] ? TrueIcon : FalseIcon}
                  alt={farmer[header] ? "Yes" : "No"}
                />
              </td>
            {:else if header === "growthRegulatorDetails"}
              <td>
                <ul>
                  {#each farmer[header].sort((a, b) => new Date(b.growthRegulatorDate).getTime() - new Date(a.growthRegulatorDate).getTime()) as { growthRegulatorDate, growthRegulatorType }}
                    <li>
                      {localizeDate(growthRegulatorDate)}: {growthRegulatorType}
                    </li>
                  {/each}
                </ul>
              </td>
            {:else}
              <td>{farmer[header]}</td>
            {/if}
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
  <Divider />
  <SectionHeader title="Transport information">
    Information about the transporting parties.
  </SectionHeader>
  <table>
    <tbody>
      {#each Object.keys(transportInformation[0]) as header}
        <tr>
          <th>
            {makeHeader(header)}
          </th>
          {#each transportInformation as transport}
            {#if header === "shipmentWeight"}
              <td>{formatNumber(transport[header], "kg")}</td>
            {:else if header === "loadingTime" || header === "unloadingTime"}
              <td>{localizeDateTime(transport[header])}</td>
            {:else if header === "previousContentDate"}
              <td>{localizeDate(transport[header])}</td>
            {:else}
              <td>{transport[header]}</td>
            {/if}
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
</Article>

<style lang="scss">
  table {
    width: 100%;
    border-collapse: collapse;
    display: block;
    overflow-x: auto;
    margin-bottom: 1rem;
  }
  th {
    font-size: 0.875rem;
    width: 230px;
    min-width: 230px;
  }
  td {
    min-width: 200px;
  }
  th,
  td {
    padding: 0.25rem 1rem 0.25rem 0.5rem;
    text-align: left;
    vertical-align: top;
  }
  td,
  li {
    font-size: 0.75rem;
  }
  img {
    width: 1rem;
  }
  ul {
    margin: 0;
    padding-left: 1rem;
  }
</style>
