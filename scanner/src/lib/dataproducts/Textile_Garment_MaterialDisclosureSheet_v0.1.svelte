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
    materials: Material[]
    chemicals?: string
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

  function formatMaterial(material: Material): string {
    let res = `${formatNumber(material.share, "%")} ${material.name}`
    if (material.recyclingRate && material.recyclingRate > 0) {
      res += ` (♺ ${formatNumber(material.recyclingRate, "%")})`
    }
    return res
  }
</script>

<Article>
  {#if outerMaterial}
    <SectionHeader title="Outer material information">
      The details of the outer materials used in the garment
    </SectionHeader>

    <div class="material-section">
      <p class="section-label">Materials:</p>
      <ul>
        {#each outerMaterial.materials as m}
          <li class="material-item">
            {formatMaterial(m)}
          </li>
        {/each}
      </ul>
    </div>

    <DataRow label="Chemicals" value={outerMaterial.chemicals} />

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

    <div class="material-section">
      <p class="section-label">Materials:</p>
      <ul>
        {#each liningMaterial.materials as m}
          <li class="material-item">
            {formatMaterial(m)}
          </li>
        {/each}
      </ul>
    </div>

    <DataRow label="Chemicals" value={liningMaterial.chemicals} />

    {#if liningMaterial.certifications.length > 0}
      <DataRow label="Certifications" value={liningMaterial.certifications.join(", ")} />
    {:else}
      <DataRow label="Certifications" value="-" />
    {/if}

    <Divider />
  {/if}

  {#if notionsMaterial}
    <SectionHeader title="Notions and trim material information">
      The details of the notions and trim materials used in the garment
    </SectionHeader>

    <div class="material-section">
      <p class="section-label">Materials:</p>
      <ul>
        {#each notionsMaterial.materials as m}
          <li class="material-item">
            {formatMaterial(m)}
          </li>
        {/each}
      </ul>
    </div>

    <DataRow label="Chemicals" value={notionsMaterial.chemicals} />

    {#if notionsMaterial.certifications.length > 0}
      <DataRow label="Certifications" value={notionsMaterial.certifications.join(", ")} />
    {:else}
      <DataRow label="Certifications" value="-" />
    {/if}
  {/if}
</Article>

<style lang="scss">
  .material-section {
    margin-bottom: 1rem;
  }

  .section-label {
    font-weight: 500;
    margin-bottom: 0.5rem;
  }

  ul {
    margin: 0;
    padding-left: 1.5rem;
  }

  .material-item {
    line-height: 150%;
  }
</style>
