<script lang="ts">
  /*
  Docs:

  https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/MetalArtifact/DataSheet_v0.1.py

  https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/MetalArtifact/DataSheet_v0.1

  https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_MetalArtifact_DataSheet_v0_1_DigitalProductPassport_MetalArtifact_DataSheet_v0_1_post
   */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"

  export let status: number
  export let data: {
    productName: string
    productType: string
    measures: {
      width: number // cm
      length: number // cm
      height: number // cm
    }
    netWeight: number // kg
    enStandardCertifications: Array<{ enStandardCode: string }>
  }
</script>

<Article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Product type" value={data.productType} />
  <DataRow label="Width" value={formatNumber(data.measures.width, "cm")} />
  <DataRow label="Length" value={formatNumber(data.measures.length, "cm")} />
  <DataRow label="Height" value={formatNumber(data.measures.height, "cm")} />
  <DataRow label="Net weight" value={formatNumber(data.netWeight, "kg")} />
  <DataRow
    label="EN Standard Code(s)"
    value={data.enStandardCertifications.map((data) => data.enStandardCode)}
  />
</Article>
