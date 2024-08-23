<script lang="ts">
  /*
    Docs:

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/RockDrill/Piston/MaterialCertificate_v0.1

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/RockDrill/Piston/MaterialCertificate_v0.1.py

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_RockDrill_Piston_MaterialCertificate_v0_1_DigitalProductPassport_RockDrill_Piston_MaterialCertificate_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import BulletedList from "$components/BulletedList/index.svelte"

  export let data: {
    productName: string
    castNumber: string
    castAnalysis: {
      element: string
      composition: number
    }[]
    inspectionConformity: {
      inspectionName: string
      inspectionDescription: string
      standardsCompliance: string[]
    }[]
  }

  const elementsMap = {
    C: "Carbon",
    Cr: "Chromium",
    Mn: "Manganese",
    Mo: "Molybdenum",
    Ni: "Nickel",
    P: "Phosphorus",
    Sf: "Sulfur",
    Si: "Silicon",
    V: "Vanadium",
  }

  function getElement(value: string): string {
    // @ts-ignore
    return elementsMap[value] || value
  }
</script>

<Article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Cast number" value={data.castNumber} />
  <Divider />
  <BulletedList title="Cast analysis" description="The material composition of the cast.">
    {#each data.castAnalysis as cast}
      <li>{getElement(cast.element)}: {formatNumber(cast.composition, "%")}</li>
    {/each}
  </BulletedList>
  {#each data.inspectionConformity as inspection}
    <Divider />
    <SectionHeader title={inspection.inspectionName}>
      <p>{inspection.inspectionDescription}</p>
      <DataRow label="Standards compliance" value={inspection.standardsCompliance.join(", ")} />
    </SectionHeader>
  {/each}
</Article>

<style lang="scss">
  p {
    margin: 0.5rem 0;
  }
</style>
