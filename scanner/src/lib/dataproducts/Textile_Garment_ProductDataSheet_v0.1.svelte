<script lang="ts">
  /*
    Docs:

    https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Textile/Garment/ProductDataSheet_v0.1.py

    https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Textile/Garment/ProductDataSheet_v0.1

    https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Textile_Garment_ProductDataSheet_v0_1_DigitalProductPassport_Textile_Garment_ProductDataSheet_v0_1_post
  */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Divider from "$components/Divider/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"

  type CompanyIdentification = {
    identifier: string
    identifierScheme: string
  }

  type BrandInformation = {
    name: string
    website?: string
    companyIdentification: CompanyIdentification
  }

  type ColorInformation = {
    colorName: string
    color?: string
    colorScheme?: string
  }

  type SizeInformation = {
    size?: string
    sizingSystem?: string
  }

  export let data: {
    brandInformation: BrandInformation
    certifications: string[]
    colorInformation: ColorInformation
    conformityDeclaration?: string
    gender?: string
    productClass: string
    productName: string
    productWebsite?: string
    regulatoryCompliance: string[]
    sizeInformation: SizeInformation
    standardsConformity: string[]
    taricCode: string
    weight?: number
  }

  const gender = data.gender
    ? data.gender.charAt(0).toUpperCase() + data.gender.slice(1)
    : "Not specified"

  function formatColor(c: ColorInformation): string {
    if (!c.color || !c.colorScheme) {
      return "Not specified"
    }
    return `${c.color} (${c.colorScheme})`
  }

  const brand = data.brandInformation
  const size = data.sizeInformation
</script>

<Article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Product class" value={data.productClass} />
  <DataRow label="Gender" value={gender} />
  {#if data.weight !== undefined}
    <DataRow label="Weight" value={formatNumber(data.weight, "kg")} />
  {/if}
  <DataRow label="TARIC code" value={data.taricCode} />
  <DataRow label="Product website" link value={data.productWebsite} />

  <Divider />

  <SectionHeader title="Brand information"
    >The details of the brand selling the garment.</SectionHeader
  >
  <DataRow label="Name" value={brand.name} />
  <DataRow label="Website" link value={brand.website} />
  <DataRow
    label="Company ID"
    value={`${brand.companyIdentification.identifier} (${brand.companyIdentification.identifierScheme})`}
  />

  <Divider />

  <SectionHeader title="Product details">The specific details of the garment</SectionHeader>

  <DataRow label="Color" value={formatColor(data.colorInformation)} />

  {#if size.size || size.sizingSystem}
    <DataRow
      label="Size"
      value={`${size.size || ""} ${size.sizingSystem ? `(${size.sizingSystem})` : ""}`}
    />
  {/if}

  <Divider />

  <SectionHeader title="Certifications and compliance">
    The certifications and compliance information of the garment
  </SectionHeader>

  <DataRow label="Certifications" value={data.certifications} />
  <DataRow label="Regulatory compliance" value={data.regulatoryCompliance} />
  <DataRow label="Standards conformity" value={data.standardsConformity} />
  <DataRow label="Conformity declaration" link value={data.conformityDeclaration} />
</Article>
