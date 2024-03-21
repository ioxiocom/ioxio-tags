<script lang="ts">
  export let noBottomPadding: boolean
</script>

<div class={"divider"} class:no-bottom-padding={noBottomPadding} />

<style lang="scss">
  .divider {
    border-bottom: 1px solid #20303e;
    margin-bottom: 1rem;
    &.no-bottom-padding {
      padding-bottom: 0;
    }
  }
</style>
