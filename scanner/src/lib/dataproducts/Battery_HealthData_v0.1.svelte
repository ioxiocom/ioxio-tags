<script lang="ts">
  /*
      Docs:

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/HealthData_v0.1.py

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/HealthData_v0.1

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_HealthData_v0_1_DigitalProductPassport_Battery_HealthData_v0_1_post
    */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"

  type OperationDetail = {
    measurementDate: string
    stateOfCharge: number
    temperature: number
  }

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

<article>
  <DataRow label="Status" value={data.status} />
  <DataRow label="Manufacturing date" value={data.manufacturingDate} />
  <DataRow label="Service initiation date" value={data.serviceInitiationDate} />
  <div class="divider" />
  <div class="title no-bottom-margin">Original performance</div>
  <div class="subtitle">The details of the original performance of the battery</div>
  <DataRow label="Capacity" value={formatNumber(data.originalPerformance.capacity, "Ah")} />
  <DataRow label="Power" value={formatNumber(data.originalPerformance.power, "Wh")} />
  <DataRow
    label="Internal resistance"
    value={formatNumber(data.originalPerformance.resistance, "Ω")}
  />
  <DataRow label="Cycle life" value={formatNumber(data.originalPerformance.cycleLife)} />
  <DataRow label="Calendar years" value={formatNumber(data.originalPerformance.years)} />
  <div class="divider" />
  <div class="title no-bottom-margin">Health state</div>
  <div class="subtitle">The state of the health of the battery</div>
  <DataRow
    label="Cumulative cycle count"
    value={formatNumber(data.healthState.cumulativeCycleCount)}
  />
  <DataRow label="Capacity fade" value={formatNumber(data.healthState.capacityFade, "%")} />
  <DataRow label="Power fade" value={formatNumber(data.healthState.powerFade, "%")} />
  <DataRow
    label="Resistance increase"
    value={formatNumber(data.healthState.resistanceIncrease, "%")}
  />
  <div class="divider" />
  <div class="title no-bottom-margin">Operation detail</div>
  <div class="subtitle">-</div>
  {#each data.healthState.operationDetails as operationDetail}
    <DataRow label="Measurement date:" value={operationDetail.measurementDate} />
    <DataRow label="State of charge" value={formatNumber(operationDetail.stateOfCharge, "Ah")} />
    <DataRow label="Temperature" value={formatNumber(operationDetail.temperature, "°C")} />
  {/each}
  <div class="divider" />
  <div class="title no-bottom-margin">Harmful events</div>
  <div class="subtitle">The harmful events or incidents that have occurred for the battery</div>
  {#each data.harmfulEvents as harmfulEvent}
    <DataRow label="Event date" value={harmfulEvent.eventDate} />
    <DataRow label="Event description" value={harmfulEvent.eventDescription} />
  {/each}
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
