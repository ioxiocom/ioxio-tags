import FoodArtifact_NutritionalValues_v0_1 from "$lib/dataproducts/FoodArtifact_NutritionalValues_v0_1.svelte"
import MetalArtifact_DataSheet_v0_1 from "$lib/dataproducts/MetalArtifact_DataSheet_v0_1.svelte"
import LogisticsEmissions_v0_1 from "$lib/dataproducts/LogisticsEmissions_v0_1.svelte"
import Battery_CarbonFootprint_v0_1 from "$lib/dataproducts/Battery_CarbonFootprint_v0_1.svelte"
import Battery_ManufacturingDataSheet_v0_1 from "$lib/dataproducts/Battery_ManufacturingDataSheet_v0.1.svelte"
import Battery_HealthData_v0_1 from "$lib/dataproducts/Battery_HealthData_v0.1.svelte"
import MobileWorkMachine_EnvironmentalFootprint_v0_1 from "$lib/dataproducts/MobileWorkMachine_EnvironmentalFootprint_v0.1.svelte"
import MobileWorkMachine_Drill_ManufacturingDataSheet_v0_2 from "$lib/dataproducts/MobileWorkMachine_Drill_ManufacturingDataSheet_v0.2.svelte"
import MobileWorkMachine_StraddleCarrier_OperationsData_v0_1 from "$lib/dataproducts/MobileWorkMachine_StraddleCarrier_OperationsData_v0.1.svelte"
export const supportedDataProducts = {
  "DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1": FoodArtifact_NutritionalValues_v0_1,
  "DigitalProductPassport/MetalArtifact/DataSheet_v0.1": MetalArtifact_DataSheet_v0_1,
  "DigitalProductPassport/LogisticsEmissions_v0.1": LogisticsEmissions_v0_1,
  "DigitalProductPassport/Battery/CarbonFootprint_v0.1": Battery_CarbonFootprint_v0_1,
  "DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1": Battery_ManufacturingDataSheet_v0_1,
  "DigitalProductPassport/Battery/HealthData_v0.1": Battery_HealthData_v0_1,
  "DigitalProductPassport/MobileWorkMachine/EnvironmentalFootprint_v0.1":
    MobileWorkMachine_EnvironmentalFootprint_v0_1,
  "DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.2":
    MobileWorkMachine_Drill_ManufacturingDataSheet_v0_2,
  "DigitalProductPassport/MobileWorkMachine/StraddleCarrier/OperationsData_v0.1":
    MobileWorkMachine_StraddleCarrier_OperationsData_v0_1,
}
