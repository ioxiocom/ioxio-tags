<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_ManufacturingDataSheet_v0_1_DigitalProductPassport_Battery_ManufacturingDataSheet_v0_1_post
     */

  import { capitaliseFirstLetter, countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import TrueIcon from "$assets/true-circle.svg"
  import FalseIcon from "$assets/false-circle.svg"
  import SectionHeader from "$components/SectionHeader/index.svelte"

  export let id: string
  export let status: number
  export let data: {
    productName: string
    batteryModel: string
    batteryCategory: string
    manufacturingDate: string
    weight: number
    capacity: number
    power: number
    cellType: string
    resistance: number
    extinguishingAgents: string[]
    warranty: string
    manufacturerInformation: {
      name: string
      streetName: string
      postalCode: string
      city: string
      country: string
      website: string
      email: string
    }
    manufacturingLocation: {
      city: string
      country: string
    }
    roundTripEfficiency: {
      initialEnergyEfficiency: number
      degradedEnergyEfficiency: number
    }
    voltageLevels: {
      nominalVoltage: number
      maximumVoltage: number
      minimumVoltage: number
    }
    temperatureRange: {
      minimumTemperature: number
      maximumTemperature: number
    }
    expectedLifetime: {
      cycleLife: number
      cycleRate: string
      referenceTest: string
    }
    materialComposition: {
      chemistry: string[]
      criticalRawMaterials: string[]
      hazardousSubstances: string[]
    }
    recycledContent: {
      substanceName: string
      recyclingRate: number
    }[]
    renewableContent: {
      substanceName: string
      proportion: number
    }[]
    legalConformity: {
      batteryActCompliance: boolean
      requirementConformity: string[]
      conformityDeclaration: string
    }
  }

  const minexpoDemo = id === "minexpo-demo-1"
</script>

<Article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Battery model" value={data.batteryModel} />
  <DataRow label="Category" value={capitaliseFirstLetter(data.batteryCategory)} />
  <DataRow label="Manufacturing date" value={data.manufacturingDate} />
  <DataRow label="Weight" value={formatNumber(data.weight, "kg")} />
  <DataRow label="Capacity" value={formatNumber(data.capacity, "Ah")} />
  <DataRow label="Power" value={formatNumber(data.power, "W")} />
  <DataRow label="Cell type" value={data.cellType} />
  <DataRow label="Resistance" value={formatNumber(data.resistance, "Ω")} />
  <DataRow label="Extinguishing agents" value={data.extinguishingAgents.join(", ")} />
  <DataRow label="Warranty valid until" value={data.warranty} />
  <Divider />
  <SectionHeader title="Manufacturer information">
    The details of the battery manufacturer
  </SectionHeader>
  <DataRow label="Name" value={data.manufacturerInformation?.name} />
  <DataRow label="Street name" value={data.manufacturerInformation?.streetName} />
  <DataRow label="Postal code" value={data.manufacturerInformation?.postalCode} />
  <DataRow label="City" value={data.manufacturerInformation?.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturerInformation?.country]} />
  {#if !minexpoDemo}
    <DataRow label="Website" column link value={data.manufacturerInformation?.website} />
    <DataRow label="Email" column value={data.manufacturerInformation?.email} />
  {/if}
  <Divider />
  {#if !minexpoDemo}
    <SectionHeader title="Manufacturing location">
      The details of the location of the battery manufacturing plant
    </SectionHeader>
    <DataRow label="City" value={data.manufacturingLocation?.city} />
    <DataRow label="Country" value={countryListAlpha3[data.manufacturingLocation?.country]} />
    <Divider />
    <SectionHeader title="Round trip efficiency">
      The details of the round trip energy efficiency in energy storages
    </SectionHeader>
    <DataRow
      label="Initial energy efficiency"
      value={formatNumber(data.roundTripEfficiency?.initialEnergyEfficiency, "%")}
    />
    <DataRow
      label="Degraded energy efficiency"
      value={formatNumber(data.roundTripEfficiency?.degradedEnergyEfficiency, "%")}
    />
    <Divider />
  {/if}
  <SectionHeader title="Voltage levels">
    The details of the voltage levels of the battery
  </SectionHeader>
  <DataRow label="Nominal" value={formatNumber(data.voltageLevels?.nominalVoltage, "V")} />
  <DataRow label="Maximum" value={formatNumber(data.voltageLevels?.maximumVoltage, "V")} />
  <DataRow label="Minimum" value={formatNumber(data.voltageLevels?.minimumVoltage, "V")} />
  <Divider />
  <SectionHeader title="Temperature range">
    The details of the acceptable temperature values of the battery
  </SectionHeader>
  <DataRow
    label="Temperature range"
    value={`${formatNumber(data.temperatureRange?.minimumTemperature, "°C")}
     to
     ${formatNumber(data.temperatureRange?.maximumTemperature, "°C")}`}
  />
  <Divider />
  {#if !minexpoDemo}
    <SectionHeader title="Expected lifetime">The details of the battery lifetime</SectionHeader>
    <DataRow label="Cycle life" value={formatNumber(data.expectedLifetime?.cycleLife)} />
    <DataRow label="Reference test" value={data.expectedLifetime?.referenceTest} />
    <DataRow label="Cycle rate" value={data.expectedLifetime?.cycleRate} />
    <Divider />
    <SectionHeader title="Material composition">
      The details of the material composition of the battery
    </SectionHeader>
    <DataRow label="Chemistry" value={data.materialComposition?.chemistry.join(", ")} />
    <DataRow
      label="Hazardous substances"
      value={data.materialComposition?.hazardousSubstances.join(", ")}
    />
    <DataRow
      label="Critical raw materials"
      value={data.materialComposition?.criticalRawMaterials.join(", ")}
    />
    <Divider />
    <SectionHeader title="Recycled content">
      The recycled content information present in the battery
    </SectionHeader>
    {#if data.recycledContent.length > 0}
      <ul>
        {#each data.recycledContent as content}
          {#if content.substanceName.trim() && content.recyclingRate}
            <li class="list-item">
              {content.substanceName}: {formatNumber(content.recyclingRate, "%")}
            </li>
          {/if}
        {/each}
      </ul>
    {:else}
      <p>-</p>
    {/if}
    <Divider />
    <SectionHeader title="Renewable content">
      The renewable content information present in the battery
    </SectionHeader>
    {#if data.renewableContent.length > 0}
      <ul>
        {#each data.renewableContent as content}
          {#if content.substanceName.trim() && content.proportion}
            <li class="list-item">
              {content.substanceName}: {formatNumber(content.proportion, "%")}
            </li>
          {/if}
        {/each}
      </ul>
    {:else}
      <p>-</p>
    {/if}
    <Divider />
  {/if}
  <SectionHeader title="Legal conformity">
    The details of the conformity of the battery with the legal and harmonized standards
  </SectionHeader>
  <div class="act-compliance">
    <p class="label">Battery act compliance:</p>
    <div class="compliance-img">
      <img
        src={data.legalConformity?.batteryActCompliance ? TrueIcon : FalseIcon}
        alt={data.legalConformity?.batteryActCompliance
          ? "Complies with the battery act"
          : "Does not comply with the battery act"}
      />
    </div>
  </div>
  <DataRow
    label="Requirement conformity"
    value={data.legalConformity?.requirementConformity.join(", ")}
  />
  <DataRow
    label="Conformity declaration"
    column
    link
    value={data.legalConformity?.conformityDeclaration}
  />
</Article>

<style lang="scss">
  .act-compliance {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    p {
      flex-grow: 0;
      flex-shrink: 0;
      flex-basis: 45%;
      line-height: 1.5rem;
      padding-right: 0.5rem;
    }

    .compliance-img {
      width: 1.5rem;
      line-height: 1.5rem;
    }
  }

  .list-item {
    line-height: 150%;
  }
</style>
