<script lang="ts">
  import { Capacitor } from "@capacitor/core"
  import { onMount } from "svelte"
  import { goto } from "$app/navigation"
  import { SvelteToast } from "@zerodevx/svelte-toast"
  import "./style.css"

  const isMobile = ["android", "ios"].indexOf(Capacitor.getPlatform()) > -1
  const maxHeight = isMobile ? "100vh" : "100svh"

  onMount(() => {
    if (isMobile) {
      goto("scan")
    }
  })
</script>

<main>
  <div class="container" style="--maxHeight: {maxHeight};">
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
    min-height: var(--maxHeight);
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
