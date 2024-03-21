<script lang="ts">
  export let noBottomMargin: boolean
  export let showDivider: boolean
</script>

<div class={"subtitle"} class:no-bottom-margin={noBottomMargin} class:divider={showDivider}>
  <slot />
</div>

<style lang="scss">
  .subtitle {
    font-size: 0.75rem;
    font-weight: 400;
    color: white;
    margin-bottom: 1rem;

    &.no-bottom-margin {
      margin-bottom: 0;
    }

    &.divider {
      padding-bottom: 1rem;
      border-bottom: 1px solid #20303e;
    }
  }
</style>
