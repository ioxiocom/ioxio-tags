<script lang="ts">
  import "./style.css"
  import { SvelteToast } from "@zerodevx/svelte-toast"
</script>

<main>
  <div class="container">
    <slot />
  </div>
  <SvelteToast />
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

  .container {
    width: 100%;
    min-height: 100svh;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    position: relative;
  }

  :global(.relative) {
    position: relative;
    z-index: 1;
  }
</style>
