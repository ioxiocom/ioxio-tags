<script lang="ts">
  /*
  Docs:

  https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/LogisticsEmissions_v0.1.py

  https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/LogisticsEmissions_v0.1

  https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_LogisticsEmissions_v0_1_DigitalProductPassport_LogisticsEmissions_v0_1_post
   */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Road from "$components/Road/index.svelte"

  type EmissionsPerTce = {
    description: string
    emissions: 1.2 // CO2e tonnes
    source: string
  }

  type RoadFreightEmissions = {
    legIdentifier: string
    origin: string
    destination: string
    freightType: string
    condition: string
    journeyType: string
    contractType: string
    totalEmissions: 5.8 // CO2e tonnes
    emissionIntensity: 200 // CO2e grams / tonne / km
    emissionsPerTce: Array<EmissionsPerTce>
  }

  type SeaFreightEmissions = {
    legIdentifier: string
    origin: string
    destination: string
    vesselType: string
    freightCondition: string
    serviceType: string
    totalEmissions: number // CO2e tonnes
    emissionIntensity: number // CO2e grams / tonne / km
    emissionsPerTce: Array<EmissionsPerTce>
  }

  export let status: number
  export let data: {
    roadFreightEmissions: Array<RoadFreightEmissions>
    seaFreightEmissions: Array<SeaFreightEmissions>
    waybillNumber: string
  }
</script>

<article>
  {#if data.roadFreightEmissions.length > 0}
    <div class="title">Road Freight Emissions</div>
    {#each data.roadFreightEmissions as roadFreightEmission}
      <div class="leg-id-label">LEG IDENTIFIER:</div>
      <div class="leg-id">{roadFreightEmission.legIdentifier}</div>
      <Road origin={roadFreightEmission.origin} destination={roadFreightEmission.destination} />
      <DataRow label="Freight type" value={roadFreightEmission.freightType} />
      <DataRow label="Condition" value={roadFreightEmission.condition} />
      <DataRow label="Journey type" value={roadFreightEmission.journeyType} />
      <DataRow label="Contract type" value={roadFreightEmission.contractType} />
      <DataRow
        label="Total emissions"
        value={formatNumber(roadFreightEmission.totalEmissions, "CO2e tonnes")}
      />
      <DataRow
        label="Emission intensity"
        value={formatNumber(roadFreightEmission.emissionIntensity, "CO2e grams / tonne / km")}
      />
      <DataRow
        label="Emissions Per TCE"
        value={[
          roadFreightEmission.emissionsPerTce[0].description,
          formatNumber(roadFreightEmission.emissionsPerTce[0].emissions, "CO2e tonnes"),
          roadFreightEmission.emissionsPerTce[0].source,
        ]}
      />
    {/each}
  {/if}
  <div class="divider" />
  {#if data.seaFreightEmissions.length > 0}
    <div class="title">Sea Freight Emissions</div>
    {#each data.seaFreightEmissions as seaFreightEmission}
      <div class="leg-id-label">LEG IDENTIFIER:</div>
      <div class="leg-id">{seaFreightEmission.legIdentifier}</div>
      <Road
        origin={seaFreightEmission.origin}
        destination={seaFreightEmission.destination}
        isTruck={false}
      />
      <DataRow label="Vessel type" value={seaFreightEmission.vesselType} />
      <DataRow label="Freight Condition" value={seaFreightEmission.freightCondition} />
      <DataRow label="Service type" value={seaFreightEmission.serviceType} />
      <DataRow
        label="Total emissions"
        value={formatNumber(seaFreightEmission.totalEmissions, "CO2e tonnes")}
      />
      <DataRow
        label="Emission intensity"
        value={formatNumber(seaFreightEmission.emissionIntensity, "CO2e grams / tonne / km")}
      />
      <DataRow
        label="Emissions Per TCE"
        value={[
          seaFreightEmission.emissionsPerTce[0].description,
          formatNumber(seaFreightEmission.emissionsPerTce[0].emissions, "CO2e tonnes"),
          seaFreightEmission.emissionsPerTce[0].source,
        ]}
      />
    {/each}
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
    }
    .leg-id-label {
      font-size: 0.75rem;
      line-height: 1.5rem;
      color: #798893;
      text-transform: uppercase;
    }
    .leg-id {
      font-size: 1rem;
      line-height: 1.5rem;
      margin-bottom: 1rem;
    }
    .divider {
      padding-bottom: 1rem;
      border-bottom: 1px solid #20303e;
      margin-bottom: 1rem;
    }
  }
</style>
