<script lang="ts">
  /*
    Docs:

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/RockDrill/DataSheet_v0.1

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/RockDrill/DataSheet_v0.1.py

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_RockDrill_DataSheet_v0_1_DigitalProductPassport_RockDrill_DataSheet_v0_1_post
  */

  import { countryListAlpha3, formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Divider from "$components/Divider/index.svelte"

  export let data: {
    productName: string
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
      country: string
      city: string
    }
    minimumHoleDiameter: number
    maximumHoleDiameter: number
    weight: number
    percussionRate: number
    drillingPower: number
    referenceDataSheet: string
    userManual: string
    safetyManual: string
  }
  const man = data.manufacturerInformation
  const location = data.manufacturingLocation
</script>

<Article>
  <DataRow label="Minimum hole diameter" value={formatNumber(data.minimumHoleDiameter, "mm")} />
  <DataRow label="Maximum hole diameter" value={formatNumber(data.maximumHoleDiameter, "mm")} />
  <DataRow label="Weight" value={formatNumber(data.weight, "kg")} />
  <DataRow label="Percussion rate" value={formatNumber(data.percussionRate, "Hz")} />
  <DataRow label="Drilling power" value={formatNumber(data.drillingPower, "kW")} />
  <DataRow label="Reference data sheet" value={data.referenceDataSheet} />
  <DataRow label="User manual" value={data.userManual} />
  <DataRow label="Safety manual" value={data.safetyManual} />
  <Divider />
  <SectionHeader title="Manufacturer information">
    <p>The details of the manufacturer.</p>
  </SectionHeader>
  <DataRow label="Name" value={man.name} />
  <DataRow label="Street name" value={man.streetName} />
  <DataRow label="Postal code" value={man.postalCode} />
  <DataRow label="City" value={man.city} />
  <DataRow label="Country" value={countryListAlpha3[man.country]} />
  <DataRow label="Website" value={man.website} />
  <DataRow label="Email" value={man.email} />
  <Divider />
  <SectionHeader title="Manufacturing location">
    <p>Location where this drill was manufactured.</p>
  </SectionHeader>
  <DataRow label="City" value={location.city} />
  <DataRow label="Country" value={countryListAlpha3[location.country]} />
</Article>

<style lang="scss">
  p {
    margin: 0.5rem 0;
  }
</style>
