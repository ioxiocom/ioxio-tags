<script lang="ts">
  /*
    Docs:

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/RockDrill/Piston/MaterialCertificate_v0.2

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/RockDrill/Piston/MaterialCertificate_v0.2.py

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_RockDrill_Piston_MaterialCertificate_v0_2_DigitalProductPassport_RockDrill_Piston_MaterialCertificate_v0_2_post
  */

  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Divider from "$components/Divider/index.svelte"

  export let data: {
    productName: string
    castNumber: string
    orderNumber: string
    castAnalysis: string
    inspectionConformity: {
      inspectionName: string
      inspectionDescription: string
      standardsCompliance: string[]
    }[]
  }
</script>

<Article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Cast number" value={data.castNumber} />
  <DataRow label="Order number" value={data.orderNumber} />
  <DataRow label="Cast analysis" value={data.castAnalysis} />
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
