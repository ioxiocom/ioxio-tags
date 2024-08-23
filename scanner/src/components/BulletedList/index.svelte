<script lang="ts">
  import SectionHeader from "$components/SectionHeader/index.svelte"

  export let title: string
  export let description = ""
</script>

<div>
  <SectionHeader {title}>
    {#if description.length > 0}
      <p>{description}</p>
    {/if}
  </SectionHeader>
  <ul>
    <slot />
  </ul>
</div>

<style lang="scss">
  ul {
    margin-top: -0.5rem;
  }

  p {
    margin-top: 0.5rem;
  }
</style>
