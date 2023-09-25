<script lang="ts">
  import "./style.css"
  import Question from "$assets/question.svg"
  import { SvelteToast } from "@zerodevx/svelte-toast"
</script>

<main>
  <div id="reader">
    <slot />
    <a class="relative documentation-wrapper" href="/">
      <img alt="question" src={Question} />
      <p class="documentation-label">Documentation</p>
    </a>
  </div>
  <SvelteToast />
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
    background: transparent;
  }

  #reader {
    width: 100%;
    height: 100vh;
    min-height: 500px;
    display: flex;
    flex-direction: column;
    padding: 1rem;
  }

  :global(.container) {
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  :global(.relative) {
    position: relative;
    z-index: 1;
  }

  .documentation-wrapper {
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 1rem;
    font-weight: bold;
    gap: 0.5rem;
  }

  .documentation-wrapper img {
    width: 2rem;
  }

  .documentation-label {
    color: white;
    font-size: 1.2rem;
  }
</style>
