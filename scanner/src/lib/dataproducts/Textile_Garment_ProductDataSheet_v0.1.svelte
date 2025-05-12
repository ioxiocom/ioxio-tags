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
    website: string
    companyIdentification: CompanyIdentification
  }

  type ColorInformation = {
    color: string
    colorScheme: string
  }

  type SizeInformation = {
    size: string
    sizingSystem: string
  }

  export let status: number

  export let data: {
    brandInformation: BrandInformation
    certifications: string[]
    colorInformation: ColorInformation
    conformityDeclaration: string
    gender: string
    productClass: string
    productName: string
    productWebsite: string
    regulatoryCompliance: string[]
    sizeInformation: SizeInformation
    standardsConformity: string[]
    taricCode: string
    weight: number
  }

  const gender = data.gender.charAt(0).toUpperCase() + data.gender.slice(1)
</script>

<Article>
  <DataRow label="Product name" value={data.productName} />
  <DataRow label="Product class" value={data.productClass} />
  <DataRow label="Gender" value={gender} />
  <DataRow label="Weight" value={formatNumber(data.weight, "kg")} />
  <DataRow label="TARIC code" value={data.taricCode} />
  <DataRow label="Product website" link value={data.productWebsite} />

  <Divider />

  <SectionHeader title="Brand information">The details of the brand</SectionHeader>
  <DataRow label="Name" value={data.brandInformation?.name} />
  <DataRow label="Website" link value={data.brandInformation?.website} />
  <DataRow
    label="Company ID"
    value={`${data.brandInformation?.companyIdentification.identifier} (${data.brandInformation?.companyIdentification.identifierScheme})`}
  />

  <Divider />

  <SectionHeader title="Product details">The specific details of the garment</SectionHeader>
  <DataRow
    label="Color"
    value={`${data.colorInformation?.color} (${data.colorInformation?.colorScheme})`}
  />
  <DataRow
    label="Size"
    value={`${data.sizeInformation?.size} (${data.sizeInformation?.sizingSystem})`}
  />

  <Divider />

  <SectionHeader title="Certifications and compliance">
    The certifications and compliance information of the garment
  </SectionHeader>

  {#if data.certifications && data.certifications.length > 0}
    <DataRow label="Certifications" value={data.certifications.join(", ")} />
  {:else}
    <DataRow label="Certifications" value="-" />
  {/if}

  {#if data.regulatoryCompliance && data.regulatoryCompliance.length > 0}
    <DataRow label="Regulatory compliance" value={data.regulatoryCompliance.join(", ")} />
  {:else}
    <DataRow label="Regulatory compliance" value="-" />
  {/if}

  {#if data.standardsConformity && data.standardsConformity.length > 0}
    <DataRow label="Standards conformity" value={data.standardsConformity.join(", ")} />
  {:else}
    <DataRow label="Standards conformity" value="-" />
  {/if}

  <DataRow label="Conformity declaration" link value={data.conformityDeclaration} />
</Article>
