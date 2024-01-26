import FoodArtifact_NutritionalValues_v0_1 from "$lib/dataproducts/FoodArtifact_NutritionalValues_v0_1.svelte"
import MetalArtifact_DataSheet_v0_1 from "$lib/dataproducts/MetalArtifact_DataSheet_v0_1.svelte"
import LogisticsEmissions_v0_1 from "$lib/dataproducts/LogisticsEmissions_v0_1.svelte"
import CarbonFootprint_v0_1 from "$lib/dataproducts/battery/CarbonFootprint_v0_1.svelte"
import BatteryManufacturingDataSheet_v0_1 from "$lib/dataproducts/battery/ManufacturingDataSheet_v0.1.svelte"
import HealthData_v0_1 from "$lib/dataproducts/battery/HealthData_v0.1.svelte"
import EnvironmentalFootprint_v0_1 from "$lib/mobile-work-machine/EnvironmentalFootprint_v0.1.svelte"
import DrillManufacturingDataSheet_v0_1 from "$lib/mobile-work-machine/DrillManufacturingDataSheet_v0.1.svelte"

export const supportedDataProducts = {
  "DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1": FoodArtifact_NutritionalValues_v0_1,
  "DigitalProductPassport/MetalArtifact/DataSheet_v0.1": MetalArtifact_DataSheet_v0_1,
  "DigitalProductPassport/LogisticsEmissions_v0.1": LogisticsEmissions_v0_1,
  "DigitalProductPassport/Battery/CarbonFootprint_v0.1": CarbonFootprint_v0_1,
  "DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1": BatteryManufacturingDataSheet_v0_1,
  "DigitalProductPassport/Battery/HealthData_v0.1": HealthData_v0_1,
  "DigitalProductPassport/MobileWorkMachine/EnvironmentalFootprint_v0.1":
    EnvironmentalFootprint_v0_1,
  "DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.1":
    DrillManufacturingDataSheet_v0_1,
}
