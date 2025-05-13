<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Textile/Garment/MaintenanceLog_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Textile/Garment/MaintenanceLog_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Textile_Garment_MaintenanceLog_v0_1_DigitalProductPassport_Textile_Garment_MaintenanceLog_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import { localizeDate } from "$lib/common"

  type Event = {
    eventDate: string
    eventDescription: string
  }

  export let data: {
    commissioningDate: string
    harmfulEvents: Event[]
    repairEvents: Event[]
    washingCycles: number
  }
</script>

<Article>
  <DataRow label="Commissioning date" value={localizeDate(data.commissioningDate)} />
  <DataRow label="Washing cycles" value={formatNumber(data.washingCycles, "")} />

  <Divider />

  <SectionHeader title="Repair Events">
    The history of repairs performed on the garment
  </SectionHeader>

  {#if data.repairEvents && data.repairEvents.length > 0}
    {#each data.repairEvents as event, index}
      <div class="event">
        <DataRow label="Date" value={localizeDate(event.eventDate)} />
        <DataRow label="Description" value={event.eventDescription} />
      </div>
      {#if index < data.repairEvents.length - 1}
        <Divider />
      {/if}
    {/each}
  {:else}
    <DataRow label="Repair events" value="No repair events recorded" />
  {/if}

  <Divider />

  <SectionHeader title="Harmful Events">
    The history of harmful events that affected the garment
  </SectionHeader>

  {#if data.harmfulEvents && data.harmfulEvents.length > 0}
    {#each data.harmfulEvents as event, index}
      <div class="event">
        <DataRow label="Date" value={localizeDate(event.eventDate)} />
        <DataRow label="Description" value={event.eventDescription} />
      </div>
      {#if index < data.harmfulEvents.length - 1}
        <Divider />
      {/if}
    {/each}
  {:else}
    <DataRow label="Harmful events" value="No harmful events recorded" />
  {/if}
</Article>

<style lang="scss">
  .event {
    margin-bottom: 1rem;
  }
</style>
