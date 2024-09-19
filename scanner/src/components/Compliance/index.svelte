<script lang="ts">
  import TrueIcon from "$assets/true-circle.svg"
  import FalseIcon from "$assets/false-circle.svg"

  export let label: string
  export let condition: boolean
  export let conformsAlt: string = "Complies"
  export let notConformsAlt: string = "Does not comply"
</script>

<div class="compliance">
  <p class="label">{label}:</p>
  <div class="compliance-img">
    <img src={condition ? TrueIcon : FalseIcon} alt={condition ? conformsAlt : notConformsAlt} />
  </div>
</div>

<style lang="scss">
  .compliance {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;

    p {
      flex-grow: 0;
      flex-shrink: 0;
      flex-basis: 45%;
      line-height: 1.5rem;
      padding-right: 0.5rem;
    }

    .compliance-img {
      width: 1.5rem;
      line-height: 1.5rem;
    }
  }
</style>
