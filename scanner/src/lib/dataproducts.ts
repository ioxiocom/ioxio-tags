import Battery_CarbonFootprint_v0_1 from "$lib/dataproducts/Battery_CarbonFootprint_v0.1.svelte"
import Battery_HealthData_v0_1 from "$lib/dataproducts/Battery_HealthData_v0.1.svelte"
import Battery_HealthData_v0_2 from "$lib/dataproducts/Battery_HealthData_v0.2.svelte"
import Battery_ManufacturingDataSheet_v0_1 from "$lib/dataproducts/Battery_ManufacturingDataSheet_v0.1.svelte"
import EnvironmentalFootprint_v0_1 from "$lib/dataproducts/EnvironmentalFootprint_v0.1.svelte"
import FoodArtifact_NutritionalValues_v0_1 from "$lib/dataproducts/FoodArtifact_NutritionalValues_v0_1.svelte"
import LogisticsEmissions_v0_1 from "$lib/dataproducts/LogisticsEmissions_v0_1.svelte"
import Machine_ComponentSerialNumbers_v0_1 from "$lib/dataproducts/Machine_ComponentSerialNumbers_v0.1.svelte"
import Machine_QualityMetrics_v0_2 from "$lib/dataproducts/Machine_QualityMetrics_v0.2.svelte"
import MetalArtifact_DataSheet_v0_1 from "$lib/dataproducts/MetalArtifact_DataSheet_v0_1.svelte"
import MobileWorkMachine_Drill_ManufacturingDataSheet_v0_2 from "$lib/dataproducts/MobileWorkMachine_Drill_ManufacturingDataSheet_v0.2.svelte"
import MobileWorkMachine_EnvironmentalFootprint_v0_1 from "$lib/dataproducts/MobileWorkMachine_EnvironmentalFootprint_v0.1.svelte"
import MobileWorkMachine_StraddleCarrier_OperationsData_v0_1 from "$lib/dataproducts/MobileWorkMachine_StraddleCarrier_OperationsData_v0.1.svelte"
import RockDrill_DataSheet_v0_1 from "$lib/dataproducts/RockDrill_DataSheet_v0.1.svelte"
import RockDrill_Piston_MaterialCertificate_v0_2 from "$lib/dataproducts/RockDrill_Piston_MaterialCertificate_v0.2.svelte"
import Product_FIBC_SustainabilityDataSheet_v0_1 from "$lib/dataproducts/Product_FIBC_SustainabilityDataSheet_v0.1.svelte"
import Product_FIBC_ProductDataSheet_v0_1 from "$lib/dataproducts/Product_FIBC_ProductDataSheet_v0.1.svelte"
import Product_GrainPassport_v0_1 from "$lib/dataproducts/Product_GrainPassport_v0.1.svelte"
import Textile_Garment_MaintenanceLog_v0_1 from "$lib/dataproducts/Textile_Garment_MaintenanceLog_v0.1.svelte"
import Textile_Garment_BillOfMaterials_v0_1 from "$lib/dataproducts/Textile_Garment_BillOfMaterials_v0.1.svelte"
import Textile_Garment_MaterialDisclosureSheet_v0_1 from "$lib/dataproducts/Textile_Garment_MaterialDisclosureSheet_v0.1.svelte"
import Textile_Garment_ManufacturerInformation_v0_1 from "$lib/dataproducts/Textile_Garment_ManufacturerInformation_v0.1.svelte"
import Textile_Garment_ProductDataSheet_v0_1 from "$lib/dataproducts/Textile_Garment_ProductDataSheet_v0.1.svelte"
import Product_CarbonFootprint_v0_1 from "$lib/dataproducts/Product_CarbonFootprint_v0.1.svelte"

export const supportedDataProducts = {
  "DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1": FoodArtifact_NutritionalValues_v0_1,
  "DigitalProductPassport/MetalArtifact/DataSheet_v0.1": MetalArtifact_DataSheet_v0_1,
  "DigitalProductPassport/LogisticsEmissions_v0.1": LogisticsEmissions_v0_1,
  "DigitalProductPassport/Battery/CarbonFootprint_v0.1": Battery_CarbonFootprint_v0_1,
  "DigitalProductPassport/Battery/ManufacturingDataSheet_v0.1": Battery_ManufacturingDataSheet_v0_1,
  "DigitalProductPassport/Battery/HealthData_v0.1": Battery_HealthData_v0_1,
  "DigitalProductPassport/Battery/HealthData_v0.2": Battery_HealthData_v0_2,
  "DigitalProductPassport/MobileWorkMachine/EnvironmentalFootprint_v0.1":
    MobileWorkMachine_EnvironmentalFootprint_v0_1,
  "DigitalProductPassport/MobileWorkMachine/Drill/ManufacturingDataSheet_v0.2":
    MobileWorkMachine_Drill_ManufacturingDataSheet_v0_2,
  "DigitalProductPassport/MobileWorkMachine/StraddleCarrier/OperationsData_v0.1":
    MobileWorkMachine_StraddleCarrier_OperationsData_v0_1,
  "DigitalProductPassport/RockDrill/Piston/MaterialCertificate_v0.2":
    RockDrill_Piston_MaterialCertificate_v0_2,
  "DigitalProductPassport/RockDrill/DataSheet_v0.1": RockDrill_DataSheet_v0_1,
  "DigitalProductPassport/EnvironmentalFootprint_v0.1": EnvironmentalFootprint_v0_1,
  "DigitalProductPassport/Machine/ComponentSerialNumbers_v0.1": Machine_ComponentSerialNumbers_v0_1,
  "DigitalProductPassport/Machine/QualityMetrics_v0.2": Machine_QualityMetrics_v0_2,
  "DigitalProductPassport/Product/FIBC/SustainabilityDataSheet_v0.1":
    Product_FIBC_SustainabilityDataSheet_v0_1,
  "DigitalProductPassport/Product/FIBC/ProductDataSheet_v0.1": Product_FIBC_ProductDataSheet_v0_1,
  "DigitalProductPassport/Product/GrainPassport_v0.1": Product_GrainPassport_v0_1,
  "DigitalProductPassport/Textile/Garment/MaintenanceLog_v0.1": Textile_Garment_MaintenanceLog_v0_1,
  "DigitalProductPassport/Textile/Garment/BillOfMaterials_v0.1":
    Textile_Garment_BillOfMaterials_v0_1,
  "DigitalProductPassport/Textile/Garment/MaterialDisclosureSheet_v0.1":
    Textile_Garment_MaterialDisclosureSheet_v0_1,
  "DigitalProductPassport/Textile/Garment/ManufacturerInformation_v0.1":
    Textile_Garment_ManufacturerInformation_v0_1,
  "DigitalProductPassport/Textile/Garment/ProductDataSheet_v0.1":
    Textile_Garment_ProductDataSheet_v0_1,
  "DigitalProductPassport/Product/CarbonFootprint_v0.1": Product_CarbonFootprint_v0_1,
}
