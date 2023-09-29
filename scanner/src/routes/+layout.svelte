<script lang="ts">
  import "./style.css"
</script>

<main>
  <slot />
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1.25rem;
    background: transparent;
  }
</style>
