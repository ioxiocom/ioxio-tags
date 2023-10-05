<script lang="ts">
  import "./style.css"
  import { SvelteToast } from "@zerodevx/svelte-toast"
</script>

<main>
  <div class="container">
    <div class="background" />
    <div id="reader">
      <slot />
    </div>
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

  #reader {
    width: 100%;
    height: 100vh;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    position: relative;
  }

  :global(.container) {
    flex: 1;
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  :global(.relative) {
    position: relative;
    z-index: 1;
  }
</style>
