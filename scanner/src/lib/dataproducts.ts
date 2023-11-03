import FoodArtifact_NutritionalValues_v0_1 from "$lib/dataproducts/FoodArtifact_NutritionalValues_v0_1.svelte"
import MetalArtifact_DataSheet_v0_1 from "$lib/dataproducts/MetalArtifact_DataSheet_v0_1.svelte"

export const supportedDataProducts = {
  "DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1": FoodArtifact_NutritionalValues_v0_1,
  "DigitalProductPassport/MetalArtifact/DataSheet_v0.1": MetalArtifact_DataSheet_v0_1,
}
