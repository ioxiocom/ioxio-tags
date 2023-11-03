<script lang="ts">
  /*
  Docs:

  https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1.py

  https://definitions.sandbox.ioxio-dataspace.com/definitions/DigitalProductPassport/FoodArtifact/NutritionalValues_v0.1

  https://gateway.sandbox.ioxio-dataspace.com/docs#/Data%20Products/DigitalProductPassport_FoodArtifact_NutritionalValues_v0_1_DigitalProductPassport_FoodArtifact_NutritionalValues_v0_1_post
   */

  import { formatNumber } from "$lib/common"

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

<article>
  <div>
    <div class="key">Energy:</div>
    <div class="value">{formatNumber(data.energyContent.energy, "kJ")}</div>
  </div>
</article>

<style lang="scss">
  article {
    color: white;

    > div {
      display: flex;
      flex-direction: row;
      gap: 2rem;
    }
  }
</style>
