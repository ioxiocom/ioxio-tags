<script lang="ts">
  /*
  Docs:

  https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1.py

  https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1

  https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_FoodArtifact_NutritionalValues_v0_1_DigitalProductPassport_FoodArtifact_NutritionalValues_v0_1_post
   */

  import { formatNumber } from "$lib/common"
  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"

  export let status: number
  export let data: {
    energyContent: {
      energy: number // kJ
      calories: number // kcal
    }
    fatContent: {
      fats: number // g / 100g
      saturatedFats: number // g / 100g
    }
    carbonHydrates: number // [sic] g / 100g
    sugar: number // g / 100g
    protein: number // g / 100g
    salt: number // g / 100g
  }
</script>

<Article>
  <DataRow label="Energy" value={formatNumber(data.energyContent.energy, "kJ")} />
  <DataRow label="Calories" value={formatNumber(data.energyContent.calories, "kcal")} />
  <DataRow label="Fats" value={formatNumber(data.fatContent.fats, "g")} />
  <DataRow label="Saturated fats" value={formatNumber(data.fatContent.saturatedFats, "g")} />
  <DataRow label="Carbohydrates" value={formatNumber(data.carbonHydrates, "g")} />
  <DataRow label="Sugar" value={formatNumber(data.sugar, "g")} />
  <DataRow label="Protein" value={formatNumber(data.protein, "g")} />
  <DataRow label="Salt" value={formatNumber(data.salt, "g")} />
</Article>
