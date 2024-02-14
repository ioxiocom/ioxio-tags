<script lang="ts">
  /*
      Docs:

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.2.py

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.2

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_MobileWorkMachine_Drill_ManufacturingDataSheet_v0_2_DigitalProductPassport_MobileWorkMachine_Drill_ManufacturingDataSheet_v0_2_post
       */

  import { capitaliseFirstLetter, countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import ElectricIcon from "$assets/fully-electric.svg"
  import HybridIcon from "$assets/hybrid.svg"
  import FuelPoweredIcon from "$assets/fuel-powered.svg"

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

<article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Boom coverage" value={formatNumber(data.boomCoverage, "m")} />
  <DataRow label="Tramming distance" value={formatNumber(data.trammingDistance, "km")} />
  <DataRow label="Maximum hole length" value={formatNumber(data.maximumHoleLength, "m")} />
  <DataRow label="Minimum hole diameter" value={formatNumber(data.minimumHoleDiameter, "mm")} />
  <DataRow label="Maximum hole diameter" value={formatNumber(data.maximumHoleDiameter, "mm")} />
  <DataRow label="Drilling power" value={formatNumber(data.drillingPower, "kW")} />
  <DataRow label="Reference data sheet" column link value={data.referenceDataSheet} />
  <DataRow label="Safety data sheet" column link value={data.safetyDataSheet} />
  <div class="divider" />
  <div class="title no-bottom-margin">Manufacturer information</div>
  <div class="subtitle">The details of the drill manufacturer</div>
  <DataRow label="Name" value={data.manufacturerInformation?.name} />
  <DataRow label="Street name" value={data.manufacturerInformation?.streetName} />
  <DataRow label="Postal code" value={data.manufacturerInformation?.postalCode} />
  <DataRow label="City" value={data.manufacturerInformation?.city} />
  <DataRow label="Country" value={countryListAlpha3[data.manufacturerInformation?.country]} />
  <DataRow label="Website" column link value={data.manufacturerInformation?.website} />
  <DataRow label="Email" column value={data.manufacturerInformation?.email} />
  <div class="divider" />
  <div class="title no-bottom-margin">Power system</div>
  <div class="subtitle">The details of the drill power system</div>
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
  <div class="divider" />
  <DataRow
    label="Electric motors"
    column
    value={data.powerSystem?.electricMotors.map((motor) => `${motor.count} x ${motor.motorType}`)}
  />
  <div class="divider no-bottom-padding" />
  <DataRow
    label="Batteries"
    column
    value={data.powerSystem?.batteries.map(
      (battery) => `${battery.count} x ${battery.cellType} ${formatNumber(battery.power, "kW")}`
    )}
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

      &.no-bottom-padding {
        padding-bottom: 0;
      }
    }

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
  }
</style>
