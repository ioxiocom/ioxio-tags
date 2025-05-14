<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Textile/Garment/MaterialDisclosureSheet_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Textile/Garment/MaterialDisclosureSheet_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Textile_Garment_MaterialDisclosureSheet_v0_1_DigitalProductPassport_Textile_Garment_MaterialDisclosureSheet_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"

  type Material = {
    name: string
    share: number
    recyclingRate?: number
  }

  type MaterialInfo = {
    name?: string
    materials: Material[]
    chemicalDisclosure?: string
    certifications: string[]
  }

  export let data: {
    outerMaterialInformation: MaterialInfo
    liningMaterialInformation: MaterialInfo
    notionsAndTrimInformation: MaterialInfo
  }

  const outerMaterial = data.outerMaterialInformation
  const liningMaterial = data.liningMaterialInformation
  const notionsMaterial = data.notionsAndTrimInformation

  function formatMaterials(materials: Material[]): string[] {
    const res: string[] = []
    for (const material of materials) {
      let s = `${formatNumber(material.share, "%")} ${material.name}`
      if (material.recyclingRate && material.recyclingRate > 0) {
        s += ` (♺ ${formatNumber(material.recyclingRate, "%")})`
      }
      res.push(s)
    }
    return res
  }
</script>

<Article>
  {#if outerMaterial}
    <SectionHeader title="Outer material information">
      The details of the outer materials used in the garment
    </SectionHeader>

    {#if outerMaterial.name}
      <DataRow label="Name" value={outerMaterial.name} />
    {/if}
    <DataRow label="Materials" value={formatMaterials(outerMaterial.materials)} />

    <DataRow label="Chemicals" value={outerMaterial.chemicalDisclosure} />

    {#if outerMaterial.certifications && outerMaterial.certifications.length > 0}
      <DataRow label="Certifications" value={outerMaterial.certifications.join(", ")} />
    {:else}
      <DataRow label="Certifications" value="-" />
    {/if}

    <Divider />
  {/if}

  {#if liningMaterial}
    <SectionHeader title="Lining material information">
      The details of the lining materials used in the garment
    </SectionHeader>

    {#if liningMaterial.name}
      <DataRow label="Name" value={liningMaterial.name} />
    {/if}
    <DataRow label="Materials" value={formatMaterials(liningMaterial.materials)} />

    <DataRow label="Chemicals" value={liningMaterial.chemicalDisclosure} />

    {#if liningMaterial.certifications.length > 0}
      <DataRow label="Certifications" value={liningMaterial.certifications.join(", ")} />
    {:else}
      <DataRow label="Certifications" value="-" />
    {/if}

    <Divider />
  {/if}

  {#if notionsMaterial && notionsMaterial.materials.length > 0}
    <SectionHeader title="Notions and trim material information">
      The details of the notions and trim materials used in the garment
    </SectionHeader>

    {#if notionsMaterial.name}
      <DataRow label="Name" value={notionsMaterial.name} />
    {/if}
    <DataRow label="Materials" value={formatMaterials(notionsMaterial.materials)} />
    <DataRow label="Chemicals" value={notionsMaterial.chemicalDisclosure} />

    {#if notionsMaterial.certifications.length > 0}
      <DataRow label="Certifications" value={notionsMaterial.certifications.join(", ")} />
    {:else}
      <DataRow label="Certifications" value="-" />
    {/if}
  {/if}
</Article>
