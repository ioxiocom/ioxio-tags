<script lang="ts">
  /*
      Docs:

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.2.py

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.2

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_MobileWorkMachine_Drill_ManufacturingDataSheet_v0_2_DigitalProductPassport_MobileWorkMachine_Drill_ManufacturingDataSheet_v0_2_post
       */

  import { capitaliseFirstLetter, countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import ElectricIcon from "$assets/fully-electric.svg"
  import HybridIcon from "$assets/hybrid.svg"
  import FuelPoweredIcon from "$assets/fuel-powered.svg"
  import SectionHeader from "$components/SectionHeader/index.svelte"

  enum PowerSystemType {
    FULLY_ELECTRIC = "fully electric",
    HYBRID = "hybrid",
    FUEL_POWERED = "fuel powered",
  }

  export let status: number

  export let data: {
    productName: string
    boomCoverage: number
    trammingDistance: number
    maximumHoleLength: number
    minimumHoleDiameter: number
    maximumHoleDiameter: number
    drillingPower: number
    referenceDataSheet: string
    safetyDataSheet: string
    manufacturerInformation: {
      name: string
      streetName: string
      postalCode: string
      city: string
      country: string
      website: string
      email: string
    }
    powerSystem: {
      type: PowerSystemType
      electricMotors: {
        motorType: string
        count: number
      }[]
      batteries: {
        power: number
        cellType: string
        count: number
      }[]
    }
  }

  let powerSystemSvg: string | null

  if (data.powerSystem.type === PowerSystemType.FULLY_ELECTRIC) {
    powerSystemSvg = ElectricIcon
  } else if (data.powerSystem.type === PowerSystemType.HYBRID) {
    powerSystemSvg = HybridIcon
  } else if (data.powerSystem.type === PowerSystemType.FUEL_POWERED) {
    powerSystemSvg = FuelPoweredIcon
  } else {
    powerSystemSvg = null
  }
</script>

<Article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Boom coverage" value={formatNumber(data.boomCoverage, "m")} />
  <DataRow label="Tramming distance" value={formatNumber(data.trammingDistance, "km")} />
  <DataRow label="Maximum hole length" value={formatNumber(data.maximumHoleLength, "m")} />
  <DataRow label="Minimum hole diameter" value={formatNumber(data.minimumHoleDiameter, "mm")} />
  <DataRow label="Maximum hole diameter" value={formatNumber(data.maximumHoleDiameter, "mm")} />
  <DataRow label="Drilling power" value={formatNumber(data.drillingPower, "kW")} />
  <DataRow label="Reference data sheet" column link value={data.referenceDataSheet} />
  <DataRow label="Safety data sheet" column link value={data.safetyDataSheet} />
  <Divider />
  <SectionHeader title="Manufacturer information">
    The details of the drill manufacturer
  </SectionHeader>
  <DataRow label="Name" value={data.manufacturerInformation?.name} />
  <DataRow label="Street name" value={data.manufacturerInformation?.streetName} />
  <DataRow label="Postal code" value={data.manufacturerInformation?.postalCode} />
  <DataRow label="City" value={data.manufacturerInformation?.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturerInformation?.country]} />
  <DataRow label="Website" column link value={data.manufacturerInformation?.website} />
  <DataRow label="Email" column value={data.manufacturerInformation?.email} />
  <Divider />
  <SectionHeader title="Power system">The details of the drill power system</SectionHeader>
  <div class="power-system-type">
    <span class="label">Type:</span>
    <div class="value">
      <div class="type-img">
        {#if powerSystemSvg}
          <img src={powerSystemSvg} alt={data.powerSystem.type} />
        {/if}
      </div>
      <span>{capitaliseFirstLetter(data.powerSystem?.type) || "-"}</span>
    </div>
  </div>
  <Divider />
  <DataRow
    label="Electric motors"
    column
    value={data.powerSystem?.electricMotors.map((motor) => `${motor.count} x ${motor.motorType}`)}
  />
  <Divider />
  <DataRow
    label="Batteries"
    column
    value={data.powerSystem?.batteries.map(
      (battery) => `${battery.count} x ${battery.cellType} ${formatNumber(battery.power, "kW")}`
    )}
  />
</Article>

<style lang="scss">
  .power-system-type {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;

    span {
      flex: 0 0 45%;
      line-height: 1.5rem;
      padding-right: 0.5rem;
    }

    .value {
      display: flex;
      flex-direction: row;
      align-items: center;

      .type-img {
        width: 1.5rem;
        line-height: 1.5rem;
        margin-right: 1rem;
      }
    }
  }
</style>
