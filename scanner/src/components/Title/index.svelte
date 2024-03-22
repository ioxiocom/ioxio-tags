<script lang="ts">
  export let noBottomMargin: boolean
</script>

<div class={"title"} class:no-bottom-margin={noBottomMargin}>
  <slot />
</div>

<style lang="scss">
  .title {
    font-size: 1rem;
    font-weight: 500;
    line-height: 1.5rem;
    margin-bottom: 1rem;

    &.no-bottom-margin {
      margin-bottom: 0;
    }
  }
</style>
