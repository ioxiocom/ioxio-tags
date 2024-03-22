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
  import Divider from "$components/Divider/index.svelte"
  import Title from "$components/Title/index.svelte"
  import Article from "$components/Article/index.svelte"

  type EmissionsPerTce = {
    description: string
    emissions: number // CO2e tonnes
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
    totalEmissions: number // CO2e tonnes
    emissionIntensity: number // CO2e grams / tonne / km
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

  const totalEmissionsRoadFreight = data.roadFreightEmissions.reduce(
    (acc, roadFreightEmission) => acc + roadFreightEmission.totalEmissions,
    0
  )
  const totalEmissionsSeaFreight = data.seaFreightEmissions.reduce(
    (acc, seaFreightEmission) => acc + seaFreightEmission.totalEmissions,
    0
  )
  const totalEmissions = totalEmissionsRoadFreight + totalEmissionsSeaFreight

  const totalEmissionsIntensityRoadFreight = data.roadFreightEmissions.reduce(
    (acc, roadFreightEmission) => acc + roadFreightEmission.emissionIntensity,
    0
  )
  const totalEmissionsIntensitySeaFreight = data.seaFreightEmissions.reduce(
    (acc, seaFreightEmission) => acc + seaFreightEmission.emissionIntensity,
    0
  )
  const totalEmissionsIntensity =
    totalEmissionsIntensityRoadFreight + totalEmissionsIntensitySeaFreight

  const averageEmissionsIntensity =
    totalEmissionsIntensity / (data.roadFreightEmissions.length + data.seaFreightEmissions.length)

  const roadEmissionSources = data.roadFreightEmissions.map((roadFreightEmission) =>
    roadFreightEmission.emissionsPerTce.map((emissionPerTce) => emissionPerTce.source)
  )
  const seaEmissionSources = data.seaFreightEmissions.map((seaFreightEmission) =>
    seaFreightEmission.emissionsPerTce.map((emissionPerTce) => emissionPerTce.source)
  )
  const emissionSources = [...new Set(roadEmissionSources.concat(seaEmissionSources).flat())]
</script>

<Article>
  {#if data.roadFreightEmissions.length > 0 || data.seaFreightEmissions.length > 0}
    <Title>Total emissions of the transports</Title>
    <Road
      origin={data.roadFreightEmissions[0].origin}
      destination={data.roadFreightEmissions[data.roadFreightEmissions.length - 1].destination}
      isTotal
    />
    <DataRow label="Total emissions" value={formatNumber(totalEmissions, "CO2e tonnes")} />
    <DataRow
      label="Average emissions intensity"
      value={formatNumber(averageEmissionsIntensity, "CO2e grams / tonne / km")}
    />

    <DataRow label="Emission sources" value={emissionSources} />
  {/if}
  <Divider />
  {#if data.roadFreightEmissions.length > 0}
    <Title>Road freight emissions</Title>
    {#each data.roadFreightEmissions as roadFreightEmission}
      <div class="leg-id-label">LEG IDENTIFIER:</div>
      <div class="leg-id">{roadFreightEmission.legIdentifier || "-"}</div>
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
        value={roadFreightEmission.emissionsPerTce
          .map((emissionPerTce) => [
            emissionPerTce.description || "",
            formatNumber(emissionPerTce.emissions, "CO2e tonnes") || "",
            emissionPerTce.source || "",
          ])
          .flat()}
      />
    {/each}
  {/if}
  <Divider />
  {#if data.seaFreightEmissions.length > 0}
    <Title>Sea freight emissions</Title>
    {#each data.seaFreightEmissions as seaFreightEmission}
      <div class="leg-id-label">LEG IDENTIFIER:</div>
      <div class="leg-id">{seaFreightEmission.legIdentifier || "-"}</div>
      <Road
        origin={seaFreightEmission.origin}
        destination={seaFreightEmission.destination}
        isTruck={false}
      />
      <DataRow label="Vessel type" value={seaFreightEmission.vesselType} />
      <DataRow label="Freight condition" value={seaFreightEmission.freightCondition} />
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
        value={seaFreightEmission.emissionsPerTce
          .map((emissionPerTce) => [
            emissionPerTce.description || "",
            formatNumber(emissionPerTce.emissions, "CO2e tonnes") || "",
            emissionPerTce.source || "",
          ])
          .flat()}
      />
    {/each}
  {/if}
</Article>

<style lang="scss">
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
</style>
