<script lang="ts">
  /*
      Docs:

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/HealthData_v0.1.py

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/HealthData_v0.1

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_HealthData_v0_1_DigitalProductPassport_Battery_HealthData_v0_1_post
    */

  import { formatNumber, localizeDate } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Common/Divider/index.svelte"
  import Title from "$components/Common/Title/index.svelte"
  import SubTitle from "$components/Common/SubTitle/index.svelte"
  import Article from "$components/Common/Article/index.svelte"

  type OperationDetail = {
    measurementDate: string
    stateOfCharge: number
    temperature: number
  }

  export let status: number
  export let data: {
    status: string
    manufacturingDate: string
    serviceInitiationDate: string
    originalPerformance: {
      capacity: number
      power: number
      resistance: number
      cycleLife: number
      years: number
    }
    healthState: {
      cumulativeCycleCount: number
      capacityFade: number
      powerFade: number
      resistanceIncrease: number
      operationDetails: OperationDetail[]
    }
    harmfulEvents: {
      eventDescription: string
      eventDate: string
    }[]
  }
</script>

<Article>
  <DataRow label="Status" value={data.status} />
  <DataRow label="Manufacturing date" value={data.manufacturingDate} />
  <DataRow label="Service initiation date" value={data.serviceInitiationDate} />
  <Divider />
  <Title class="no-bottom-margin">Original performance</Title>
  <SubTitle>The details of the original performance of the battery</SubTitle>
  <DataRow label="Capacity" value={formatNumber(data.originalPerformance?.capacity, "Ah")} />
  <DataRow label="Power" value={formatNumber(data.originalPerformance?.power, "W")} />
  <DataRow
    label="Internal resistance"
    value={formatNumber(data.originalPerformance?.resistance, "Ω")}
  />
  <DataRow label="Cycle life" value={formatNumber(data.originalPerformance?.cycleLife)} />
  <DataRow
    label="Expected lifetime"
    value={formatNumber(data.originalPerformance?.years, "years")}
  />
  <Divider />
  <Title class="no-bottom-margin">Health state</Title>
  <SubTitle>The state of the health of the battery</SubTitle>
  <DataRow
    label="Cumulative cycle count"
    value={formatNumber(data.healthState?.cumulativeCycleCount)}
  />
  <DataRow label="Capacity fade" value={formatNumber(data.healthState?.capacityFade, "%")} />
  <DataRow label="Power fade" value={formatNumber(data.healthState?.powerFade, "%")} />
  <DataRow
    label="Resistance increase"
    value={formatNumber(data.healthState?.resistanceIncrease, "%")}
  />
  <Divider />
  <Title class="no-bottom-margin">Operation details</Title>
  <SubTitle>The periodic information of the battery operation</SubTitle>
  {#if data.healthState?.operationDetails.length > 0}
    <div class="grid">
      <SubTitle class="no-bottom-margin">Measurement date</SubTitle>
      <SubTitle class="no-bottom-margin">State of charge</SubTitle>
      <SubTitle class="no-bottom-margin">Temperature</SubTitle>
      {#each data.healthState.operationDetails as operationDetail}
        <div>{localizeDate(operationDetail.measurementDate) || "-"}</div>
        <div>{formatNumber(operationDetail.stateOfCharge, "Ah")}</div>
        <div>{formatNumber(operationDetail.temperature, "°C")}</div>
      {/each}
    </div>
  {:else}
    <span>-</span>
  {/if}
  <Divider />
  <Title class="no-bottom-margin">Harmful events</Title>
  <SubTitle>The harmful events or incidents that have occurred for the battery</SubTitle>
  {#if data.harmfulEvents.length > 0}
    {#each data.harmfulEvents as harmfulEvent}
      {#if harmfulEvent.eventDescription.trim() && harmfulEvent.eventDate.trim()}
        <DataRow
          label={localizeDate(harmfulEvent.eventDate)}
          value={harmfulEvent.eventDescription}
        />
      {/if}
    {/each}
  {:else}
    <span>-</span>
  {/if}
</Article>

<style lang="scss">
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1rem;
    @media screen and (max-width: 389px) {
      text-align: center;
    }
  }
</style>
