<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_ManufacturingDataSheet_v0_1_DigitalProductPassport_Battery_ManufacturingDataSheet_v0_1_post
     */

  import { countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import True from "$assets/true-circle.svg"
  import False from "$assets/false-circle.svg"

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
      initialEnergyEfficieny: number
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
</script>

<article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Battery model" value={data.batteryModel} />
  <DataRow label="Battery category" value={data.batteryCategory} />
  <DataRow label="Manufacturing date" value={data.manufacturingDate} />
  <DataRow label="Weight" value={formatNumber(data.weight, "kg")} />
  <DataRow label="Capacity" value={formatNumber(data.capacity, "Ah")} />
  <DataRow label="Power" value={formatNumber(data.power, "W")} />
  <DataRow label="Cell type" value={data.cellType} />
  <DataRow label="Resistance" value={formatNumber(data.resistance, "Ω")} />
  <DataRow label="Extinguishing agents" value={data.extinguishingAgents.join(", ")} />
  <DataRow label="Warranty valid until" value={data.warranty} />
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturer information</div>
  <div class="subtitle">The details of the battery manufacturer</div>
  <DataRow label="Name" value={data.manufacturerInformation.name} />
  <DataRow label="Street name" value={data.manufacturerInformation.streetName} />
  <DataRow label="Postal code" value={data.manufacturerInformation.postalCode} />
  <DataRow label="City" value={data.manufacturerInformation.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturerInformation.country]} />
  <DataRow label="Website" column link value={data.manufacturerInformation.website} />
  <DataRow label="Email" column value={data.manufacturerInformation.email} />
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturing location</div>
  <div class="subtitle">The details of the location of the battery manufacturing plant</div>
  <DataRow label="City" value={data.manufacturingLocation.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturingLocation.country]} />
  <div class="divider" />
  <div class="title no-bottom-margin">Round trip efficiency</div>
  <div class="subtitle">The details of the round trip energy efficiency in energy storages</div>
  <DataRow
    label="Initial energy efficiency"
    value={formatNumber(data.roundTripEfficiency.initialEnergyEfficieny, "%")}
  />
  <DataRow
    label="Degraded energy efficiency"
    value={formatNumber(data.roundTripEfficiency.degradedEnergyEfficiency, "%")}
  />
  <div class="divider" />
  <div class="title no-bottom-margin">Voltage levels</div>
  <div class="subtitle">The details of the voltage levels of the battery</div>
  <DataRow label="Nominal" value={`${formatNumber(data.voltageLevels.nominalVoltage, "V")}`} />
  <DataRow label="Maximum" value={`${formatNumber(data.voltageLevels.maximumVoltage, "V")}`} />
  <DataRow label="Minimum" value={`${formatNumber(data.voltageLevels.minimumVoltage, "V")}`} />
  <div class="divider" />
  <div class="title no-bottom-margin">Temperature range</div>
  <div class="subtitle">The details of the acceptable temperature values of the battery</div>
  <DataRow
    label="Temperature range"
    value={`${formatNumber(data.temperatureRange.minimumTemperature, "°C")} to ${formatNumber(
      data.temperatureRange.maximumTemperature,
      "°C"
    )}`}
  />
  <div class="divider" />
  <div class="title no-bottom-margin">Expected lifetime</div>
  <div class="subtitle">The details of the battery lifetime</div>
  <DataRow label="Cycle life" value={formatNumber(data.expectedLifetime.cycleLife)} />
  <DataRow label="Reference test" value={data.expectedLifetime.referenceTest} />
  <DataRow label="Cycle rate" value={data.expectedLifetime.cycleRate} />
  <div class="divider" />
  <div class="title no-bottom-margin">Material composition</div>
  <div class="subtitle">The details of the material composition of the battery</div>
  <DataRow label="Chemistry" value={data.materialComposition.chemistry.join(", ")} />
  <DataRow
    label="Hazardous substances"
    value={data.materialComposition.hazardousSubstances.join(", ")}
  />
  <DataRow
    label="Critical raw materials"
    value={data.materialComposition.criticalRawMaterials.join(", ")}
  />
  <div class="divider" />
  <div class="title no-bottom-margin">Recycled content</div>
  <div class="subtitle">The recycled content information present in the battery</div>
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
  <div class="divider" />
  <div class="title no-bottom-margin">Renewable content</div>
  <div class="subtitle">The renewable content information present in the battery</div>
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
  <div class="divider" />
  <div class="title no-bottom-margin">Legal conformity</div>
  <div class="subtitle">
    The details of the conformity of the battery with the legal and harmonized standards
  </div>
  <div class="act-compliance">
    <p class="label">Battery act compliance:</p>
    <div class="compliance-img">
      <img src={data.legalConformity.batteryActCompliance ? True : False} alt="compliance status" />
    </div>
  </div>
  <DataRow
    label="Requirement conformity"
    value={data.legalConformity.requirementConformity.join(", ")}
  />
  <DataRow
    label="Conformity declaration"
    column
    link
    value={data.legalConformity.conformityDeclaration}
  />
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
      border-bottom: 1px solid #20303e;
      margin-bottom: 1rem;
    }

    .act-compliance {
      display: flex;
      align-items: center;
      margin-bottom: 1rem;
      p {
        flex: 0 0 45%;
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
  }
</style>
