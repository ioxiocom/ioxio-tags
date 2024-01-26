<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Battery_ManufacturingDataSheet_v0_1_DigitalProductPassport_Battery_ManufacturingDataSheet_v0_1_post
     */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"

  export let data: {
    productName: string
    batteryModel: string
    batteryCategory: string
    manufacturingDate: string
    weight: number
    capacity: number
    power: number
    extinguishingAgents: string[]
    warranty: string
    manufacturerInformation: {
      name: string
      postalCode: string
      city: string
      country: string
      website: string
      email: string
    }
    manufacturingLocation: {
      country: string
      city: string
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
    legalConformity: {
      requirementConformity: string[]
      conformityDeclaration: string
    }
  }

  function camelCaseToWords(s: string) {
    const result = s.replace(/([A-Z])/g, " $1")
    return result.charAt(0).toUpperCase() + result.slice(1)
  }
  console.log(data)
</script>

<article>
  <DataRow label="Product Name" value={data.productName} />
  <DataRow label="Battery Model" value={data.batteryModel} />
  <DataRow label="Battery Category" value={data.batteryCategory} />
  <DataRow label="Manufacturing Date" value={data.manufacturingDate} />
  <DataRow label="Weight" value={formatNumber(data.weight, "kg")} />
  <DataRow label="Capacity" value={formatNumber(data.capacity, "Ah")} />
  <DataRow label="Power" value={formatNumber(data.power, "Ah")} />
  <DataRow label="Extinguishing Agents" value={data.extinguishingAgents.join(", ")} />
  <DataRow label="Warranty" value={data.warranty} />
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturer Location</div>
  <div class="subtitle">The details of the battery manufacturer</div>
  {#each Object.entries(data.manufacturerInformation) as [key, value]}
    <DataRow label={camelCaseToWords(key)} {value} />
  {/each}
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturing Location</div>
  <div class="subtitle">The details of the location of the battery manufacturing plant</div>
  {#each Object.entries(data.manufacturingLocation) as [key, value]}
    <DataRow label={camelCaseToWords(key)} {value} />
  {/each}
  <div class="divider" />
  <div class="title no-bottom-margin">Round Trip Efficiency</div>
  <div class="subtitle">The details of the round trip energy efficiency in energy storages</div>
  {#each Object.entries(data.roundTripEfficiency) as [key, value]}
    <DataRow label={camelCaseToWords(key)} value={formatNumber(value, "%")} />
  {/each}
  <div class="divider" />
  <div class="title no-bottom-margin">Voltage Levels</div>
  <div class="subtitle">The details of the voltage levels of the battery</div>
  {#each Object.entries(data.voltageLevels) as [key, value]}
    <DataRow label={camelCaseToWords(key)} value={formatNumber(value, "V")} />
  {/each}
  <div class="divider" />
  <div class="title no-bottom-margin">Temperature Range</div>
  <div class="subtitle">The details of the acceptable temperature values of the battery</div>
  {#each Object.entries(data.temperatureRange) as [key, value]}
    <DataRow label={camelCaseToWords(key)} value={formatNumber(value, "C°")} />
  {/each}
  <div class="divider" />
  <div class="title no-bottom-margin">Expected Lifetime</div>
  <div class="subtitle">The details of the battery lifetime</div>
  <DataRow label="Cycle Life" value={formatNumber(data.expectedLifetime.cycleLife)} />
  <DataRow label="Reference Test" value={data.expectedLifetime.referenceTest} />
  <DataRow label="Cycle Rate" value={data.expectedLifetime.cycleRate} />
  <div class="divider" />
  <div class="title no-bottom-margin">Material Composition</div>
  <div class="subtitle">The details of the material composition of the battery</div>
  <div class="divider" />
  <div class="title no-bottom-margin">Extinguishing Agents</div>
  <div class="subtitle">
    The type of the fire extinguishing agent that can be used for the battery
  </div>
  <DataRow
    label="Requirement Conformity"
    value={data.legalConformity.requirementConformity.join(", ")}
  />
  <DataRow label="Conformity Declaration" link value={data.legalConformity.conformityDeclaration} />
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
