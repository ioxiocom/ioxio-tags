<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Textile/Garment/ManufacturerInformation_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Textile/Garment/ManufacturerInformation_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Textile_Garment_ManufacturerInformation_v0_1_DigitalProductPassport_Textile_Garment_ManufacturerInformation_v0_1_post
  */

  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import { countryListAlpha3, localizeDate } from "$lib/common"

  type Location = {
    city?: string
    country: string
  }

  type Manufacturer = {
    facilityId?: string
    manufacturerName: string
    manufacturingDate: string
    manufacturingLocation: Location
    manufacturingPhase: string
  }

  export let data: {
    manufacturers: Manufacturer[]
  }

  function formatLocation(location: Location): string {
    if (location.city) {
      return `${location.city}, ${countryListAlpha3[location.country]}`
    }
    return countryListAlpha3[location.country]
  }
</script>

<Article>
  {#if data.manufacturers.length > 0}
    {#each data.manufacturers as m, index}
      <div class="manufacturer">
        <DataRow label="Manufacturer name" value={m.manufacturerName} />
        <DataRow label="Facility ID" value={m.facilityId} />
        <DataRow label="Manufacturing date" value={localizeDate(m.manufacturingDate)} />
        <DataRow label="Manufacturing location" value={formatLocation(m.manufacturingLocation)} />
        <DataRow label="Manufacturing phase" value={m.manufacturingPhase} />
      </div>
      {#if index < data.manufacturers.length - 1}
        <Divider />
      {/if}
    {/each}
  {:else}
    <DataRow label="Manufacturers" value="No manufacturer information available" />
  {/if}
</Article>
