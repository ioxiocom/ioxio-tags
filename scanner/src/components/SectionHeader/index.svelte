<script lang="ts">
  export let title
</script>

<div class="title">
  {title}
</div>
<div class="subtitle">
  <slot />
</div>

<style lang="scss">
  .title {
    font-size: 1rem;
    font-weight: 500;
    line-height: 1.5rem;
  }
  .subtitle {
    font-size: 0.75rem;
    font-weight: 400;
    color: white;
    margin-bottom: 1rem;
  }
</style>
