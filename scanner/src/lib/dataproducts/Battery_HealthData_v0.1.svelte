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
  <DataRow label="Manufacturing Date" value={data.manufacturingDate} />
  <DataRow label="Service Initiation Date" value={data.serviceInitiationDate} />
  <div class="divider" />
  <div class="title no-bottom-margin">Original Performance</div>
  <div class="subtitle">The details of the original performance of the battery</div>
  <DataRow label="Capacity" value={formatNumber(data.originalPerformance.capacity, "Ah")} />
  <DataRow label="Power" value={formatNumber(data.originalPerformance.power, "Wh")} />
  <DataRow
    label="Internal Resistance"
    value={formatNumber(data.originalPerformance.resistance, "Ω")}
  />
  <DataRow label="Cycle Life" value={formatNumber(data.originalPerformance.cycleLife)} />
  <DataRow label="Calendar Years" value={formatNumber(data.originalPerformance.years)} />
  <div class="divider" />
  <div class="title no-bottom-margin">Health State</div>
  <div class="subtitle">The state of the health of the battery</div>
  <DataRow
    label="Cumulative Cycle Count"
    value={formatNumber(data.healthState.cumulativeCycleCount)}
  />
  <DataRow label="Capacity Fade" value={formatNumber(data.healthState.capacityFade, "%")} />
  <DataRow label="Power Fade" value={formatNumber(data.healthState.powerFade, "%")} />
  <DataRow
    label="Resistance Increase"
    value={formatNumber(data.healthState.resistanceIncrease, "%")}
  />
  {#each data.healthState.operationDetails as operationDetail}
    <DataRow label="Measurement Date:" value={operationDetail.measurementDate} />
    <DataRow label="State of Charge" value={formatNumber(operationDetail.stateOfCharge, "Ah")} />
    <DataRow label="Temperature" value={formatNumber(operationDetail.temperature, "C°")} />
  {/each}
  <div class="divider" />
  <div class="title no-bottom-margin">Harmful Events</div>
  <div class="subtitle">The harmful events or incidents that have occurred for the battery</div>
  {#each data.harmfulEvents as harmfulEvent}
    <DataRow label="Event Date" value={harmfulEvent.eventDate} />
    <DataRow label="Event Description" value={harmfulEvent.eventDescription} />
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
