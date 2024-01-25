import FoodArtifact_NutritionalValues_v0_1 from "$lib/dataproducts/FoodArtifact_NutritionalValues_v0_1.svelte"
import MetalArtifact_DataSheet_v0_1 from "$lib/dataproducts/MetalArtifact_DataSheet_v0_1.svelte"
import LogisticsEmissions_v0_1 from "$lib/dataproducts/LogisticsEmissions_v0_1.svelte"
import CarbonFootprint_v0_1 from "$lib/dataproducts/CarbonFootprint_v0_1.svelte"
import ManufacturingDataSheet_v0_1 from "$lib/dataproducts/ManufacturingDataSheet_v0.1.svelte"

export const supportedDataProducts = {
  "DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1": FoodArtifact_NutritionalValues_v0_1,
  "DigitalProductPassport/MetalArtifact/DataSheet_v0.1": MetalArtifact_DataSheet_v0_1,
  "DigitalProductPassport/LogisticsEmissions_v0.1": LogisticsEmissions_v0_1,
  "DigitalProductPassport/Battery/CarbonFootprint_v0.1": CarbonFootprint_v0_1,
  "DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1": ManufacturingDataSheet_v0_1,
}
