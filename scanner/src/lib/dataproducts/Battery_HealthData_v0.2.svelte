<script lang="ts">
  /*
      Docs:

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/HealthData_v0.2.py

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/HealthData_v0.2

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_HealthData_v0_2_DigitalProductPassport_Battery_HealthData_v0_2_post
    */

  import { formatNumber, localizeDate } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Subtitle from "$components/Subtitle/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Compliance from "$components/Compliance/index.svelte"

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
      actualCurrent: number
      actualPower: number
      actualVoltage: number
      operationDetails: {
        measurementDate: string
        chargePercentage: number
        temperature: number
      }[]
    }
    harmfulEvents: {
      eventDescription: string
      eventDate: string
    }[]
  }
</script>

<Article>
  <Compliance
    label="Status"
    condition={data.status === "original"}
    conformsAlt="Original"
    notConformsAlt="Not original"
  />
  <DataRow label="Manufacturing date" value={data.manufacturingDate} />
  <DataRow label="Service initiation date" value={data.serviceInitiationDate} />
  <Divider />
  <SectionHeader title="Original performance">
    The details of the original performance of the battery
  </SectionHeader>
  <DataRow label="Capacity" value={formatNumber(data.originalPerformance?.capacity, "Ah")} />
  <Divider />
  <SectionHeader title="Health state">The state of the health of the battery</SectionHeader>
  <DataRow label="Current" value={formatNumber(data.healthState.actualCurrent, "A")} />
  <DataRow label="Power" value={formatNumber(data.healthState.actualPower / 1000, "kW")} />
  <DataRow label="Voltage" value={formatNumber(data.healthState.actualVoltage, "V")} />
  <Divider />
  <SectionHeader title="Operation details">
    The periodic information of the battery operation
  </SectionHeader>
  {#if data.healthState?.operationDetails.length > 0}
    <div class="grid">
      <Subtitle>State of charge</Subtitle>
      <Subtitle>Temperature</Subtitle>
      {#each data.healthState.operationDetails as operationDetail}
        <div>{formatNumber(operationDetail.chargePercentage, "%")}</div>
        <div>{formatNumber(operationDetail.temperature, "°C")}</div>
      {/each}
    </div>
  {:else}
    <span>-</span>
  {/if}
</Article>

<style lang="scss">
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1rem;

    @media screen and (max-width: 389px) {
      :global(.subtitle) {
        text-align: center;
      }
    }
  }
</style>
