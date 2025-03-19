<script lang="ts">
  /*
      Docs:

      https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/Product/FIBC/ProductDataSheet_v0.1

      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Product/FIBC/ProductDataSheet_v0.1.py

      https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_Product_FIBC_ProductDataSheet_v0_1_DigitalProductPassport_Product_FIBC_ProductDataSheet_v0_1_post
    */

  import { formatNumber, countryListAlpha3, localizeDate } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import SectionHeader from "$components/SectionHeader/index.svelte"
  import Divider from "$components/Divider/index.svelte"

  enum FIBCType {
    A = "A",
    B = "B",
    C = "C",
    D = "D",
  }

  enum FillingMethod {
    TOP = "Top",
    BOTTOM = "Bottom",
  }

  export let data: {
    model: string
    type: FIBCType
    safeWorkingLoad: number
    fillingMethod: FillingMethod
    uvProtected: boolean
    uvGuaranteeYears: number
    materialComposition: string
    manufacturingInformation: {
      manufacturer: string
      batchNumber: string
      manufacturingDate: string
      expirationDate: string
      productionCity: string
      productionCountry: string
      safetyFactor: string
      complianceCertifications: string[]
    }
    dimensions: {
      externalWidth: number
      externalLength: number
      externalHeight: number
      internalWidth: number
      internalLength: number
      internalHeight: number
      volume: number
    }
    loops: {
      type: string
      height: number
      color: string
    }
    body: {
      stitching: string
      stitchingColor: string
      coatingApplied: boolean
      color: string
    }
    topSpout: {
      diameter: number
      length: number
      coatingApplied: boolean
      color: string
    }
    bottom: {
      diameter: number
      length: number
      coatingApplied: boolean
      color: string
    }
    liner: {
      type: string
      thickness: number
      color: string
    }
    documentPocket: string
    handlingInstructions: string
    inspectionDate: string
    typeMarkings: string[]
    foodSafe: boolean
  }

  const { manufacturingInformation, dimensions, loops, body, topSpout, bottom, liner } = data
</script>

<Article>
  <DataRow label="Model" value={data.model} />
  <DataRow label="Type" value={data.type} />
  <DataRow label="Safe working load" value={formatNumber(data.safeWorkingLoad, "kg")} />
  <DataRow label="Filling method" value={data.fillingMethod} />
  <DataRow label="UV protected" value={data.uvProtected} />
  <DataRow label="UV guarantee years" value={formatNumber(data.uvGuaranteeYears)} />
  <DataRow label="Material composition" value={data.materialComposition} />
  <Divider />
  <SectionHeader title="Manufacturing information">
    The manufacturing details of the bag.
  </SectionHeader>
  <DataRow label="Manufacturer" value={manufacturingInformation.manufacturer} />
  <DataRow label="Batch number" value={manufacturingInformation.batchNumber} />
  <DataRow
    label="Manufacturing date"
    value={localizeDate(manufacturingInformation.manufacturingDate)}
  />
  <DataRow label="Expiration date" value={localizeDate(manufacturingInformation.expirationDate)} />
  <DataRow label="Production city" value={manufacturingInformation.productionCity} />
  <DataRow
    label="Production country"
    value={countryListAlpha3[manufacturingInformation.productionCountry]}
  />
  <DataRow label="Safety factor" value={manufacturingInformation.safetyFactor} />
  <DataRow
    label="Compliance certifications"
    value={manufacturingInformation.complianceCertifications}
  />
  <Divider />
  <SectionHeader title="Dimensions">The dimensions of the bag.</SectionHeader>
  <DataRow label="External width" value={formatNumber(dimensions.externalWidth, "cm")} />
  <DataRow label="External length" value={formatNumber(dimensions.externalLength, "cm")} />
  <DataRow label="External height" value={formatNumber(dimensions.externalHeight, "cm")} />
  <DataRow label="Internal width" value={formatNumber(dimensions.internalWidth, "cm")} />
  <DataRow label="Internal length" value={formatNumber(dimensions.internalLength, "cm")} />
  <DataRow label="Internal height" value={formatNumber(dimensions.internalHeight, "cm")} />
  <DataRow label="Volume" value={formatNumber(dimensions.volume, "m³")} />
  <Divider />
  <SectionHeader title="Loops">Description of the loops of the bag.</SectionHeader>
  <DataRow label="Type" value={loops.type} />
  <DataRow label="Height" value={formatNumber(loops.height, "cm")} />
  <DataRow label="Color" value={loops.color} />
  <Divider />
  <SectionHeader title="Body">Description of the body of the bag.</SectionHeader>
  <DataRow label="Color" value={body.color} />
  <DataRow label="Coating applied" value={body.coatingApplied} />
  <DataRow label="Stitching" value={body.stitching} />
  <DataRow label="Stitching color" value={body.stitchingColor} />
  <Divider />
  {#if data.topSpout}
    <SectionHeader title="Top spout">Description of the top spout of the bag.</SectionHeader>
    <DataRow label="Diameter" value={formatNumber(topSpout.diameter, "cm")} />
    <DataRow label="Length" value={formatNumber(topSpout.length, "cm")} />
    <DataRow label="Color" value={topSpout.color} />
    <DataRow label="Coating applied" value={topSpout.coatingApplied} />
    <Divider />
  {/if}
  {#if data.bottom}
    <SectionHeader title="Bottom spout">Description of the bottom spout of the bag.</SectionHeader>
    <DataRow label="Diameter" value={formatNumber(bottom.diameter, "cm")} />
    <DataRow label="Length" value={formatNumber(bottom.length, "cm")} />
    <DataRow label="Color" value={bottom.color} />
    <DataRow label="Coating applied" value={bottom.coatingApplied} />
    <Divider />
  {/if}
  <SectionHeader title="Liner">Description of the liner of the bag.</SectionHeader>
  <DataRow label="Type" value={liner.type} />
  <DataRow label="Thickness" value={formatNumber(liner.thickness, "µm")} />
  <DataRow label="Color" value={liner.color} />
  <Divider />
  <DataRow label="Document pocket" value={data.documentPocket} />
  <DataRow label="Handling instructions" value={data.handlingInstructions} />
  <DataRow label="Inspection date" value={localizeDate(data.inspectionDate)} />
  <DataRow label="Type markings" value={data.typeMarkings} />
  <DataRow label="Food safe" value={data.foodSafe} />
</Article>
