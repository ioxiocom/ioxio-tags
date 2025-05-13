<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Textile/Garment/BillofMaterials_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Textile/Garment/BillofMaterials_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Textile_Garment_BillofMaterials_v0_1_DigitalProductPassport_Textile_Garment_BillofMaterials_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"

  type MaterialInfo = {
    name: string
    share: number
    recyclingRate?: number
  }

  type ChemicalInfo = {
    chemicalIdentifier: string
    classificationSystem: string
  }

  type ColorInfo = {
    color?: string
    colorScheme?: string
  }

  type Component = {
    name: string
    type: string
    materials: MaterialInfo[]
    chemicals: ChemicalInfo[]
    colorInformation?: ColorInfo
  }

  export let status: number

  export let data: {
    outerComponents: Component[]
    liningComponents: Component[]
    notionsAndTrimComponents: Component[]
  }

  function formatMaterial(material: MaterialInfo): string {
    let res = `${formatNumber(material.share, "%")} ${material.name}`
    if (material.recyclingRate && material.recyclingRate > 0) {
      res += ` (♺ ${formatNumber(material.recyclingRate, "%")})`
    }
    return res
  }

  function formatColor(c: ColorInfo): string {
    if (!c.color || !c.colorScheme) {
      return "Not specified"
    }
    return `${c.color} (${c.colorScheme})`
  }

  function formatChemical(c: ChemicalInfo): string {
    return `${c.chemicalIdentifier} (${c.classificationSystem.toUpperCase()})`
  }
</script>

<Article>
  {#if data.outerComponents && data.outerComponents.length > 0}
    <SectionHeader title="Outer Components">
      The details of the outer components used in the garment
    </SectionHeader>
    {#each data.outerComponents as с, index}
      <div class="component">
        <DataRow label="Name" value={с.name} />
        <DataRow label="Type" value={с.type} />
        {#if с.colorInformation}
          <DataRow label="Color" value={formatColor(с.colorInformation)} />
        {/if}
        <div class="bullet-list-section">
          <p class="bullet-list-header">Materials:</p>
          <ul>
            {#each с.materials as material}
              <li class="bullet-list-item">
                {formatMaterial(material)}
              </li>
            {/each}
          </ul>
        </div>
        <div class="bullet-list-section">
          <p class="bullet-list-header">Chemicals:</p>
          <ul>
            {#each с.chemicals as chemical}
              <li class="bullet-list-item">
                {formatChemical(chemical)}
              </li>
            {/each}
          </ul>
        </div>
      </div>
      {#if index < data.outerComponents.length - 1}
        <Divider />
      {/if}
    {/each}
    <Divider />
  {/if}

  {#if data.liningComponents && data.liningComponents.length > 0}
    <SectionHeader title="Lining Components">
      The details of the lining components used in the garment
    </SectionHeader>
    {#each data.liningComponents as c, index}
      <div class="component">
        <DataRow label="Name" value={c.name} />
        <DataRow label="Type" value={c.type} />
        {#if c.colorInformation}
          <DataRow label="Color" value={formatColor(c.colorInformation)} />
        {/if}
        <div class="bullet-list-section">
          <p class="bullet-list-header">Materials:</p>
          <ul>
            {#each c.materials as material}
              <li class="bullet-list-item">
                {formatMaterial(material)}
              </li>
            {/each}
          </ul>
        </div>
        <div class="bullet-list-section">
          <p class="bullet-list-header">Chemicals:</p>
          <ul>
            {#each c.chemicals as chemical}
              <li class="bullet-list-item">
                {formatChemical(chemical)}
              </li>
            {/each}
          </ul>
        </div>
      </div>
      {#if index < data.liningComponents.length - 1}
        <Divider />
      {/if}
    {/each}
    <Divider />
  {/if}

  {#if data.notionsAndTrimComponents && data.notionsAndTrimComponents.length > 0}
    <SectionHeader title="Notions & Trim Components">
      The details of the notions and trim components used in the garment
    </SectionHeader>
    {#each data.notionsAndTrimComponents as c, index}
      <div class="component">
        <DataRow label="Name" value={c.name} />
        <DataRow label="Type" value={c.type} />
        {#if c.colorInformation}
          <DataRow label="Color" value={formatColor(c.colorInformation)} />
        {/if}
        <div class="bullet-list-section">
          <p class="bullet-list-header">Materials:</p>
          <ul>
            {#each c.materials as material}
              <li class="bullet-list-item">
                {formatMaterial(material)}
              </li>
            {/each}
          </ul>
        </div>
        <div class="bullet-list-section">
          <p class="bullet-list-header">Chemicals:</p>
          <ul>
            {#each c.chemicals as chemical}
              <li class="bullet-list-item">
                {formatChemical(chemical)}
              </li>
            {/each}
          </ul>
        </div>
      </div>
      {#if index < data.notionsAndTrimComponents.length - 1}
        <Divider />
      {/if}
    {/each}
  {/if}
</Article>

<style lang="scss">
  .component {
    margin-bottom: 1rem;
  }

  .bullet-list-section {
    margin-top: 0.5rem;
    margin-bottom: 1rem;
  }

  .bullet-list-header {
    flex: 0 0 45%;
    line-height: 1.5rem;
    margin-bottom: 0.5rem;
    font-weight: 500;
  }

  ul {
    margin: 0;
    padding-left: 1.5rem;
  }

  .bullet-list-item {
    line-height: 150%;
  }
</style>
