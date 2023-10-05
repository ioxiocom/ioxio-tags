<script lang="ts">
  import LeftArrowSvg from "$assets/left-arrow.svg"
  import QuestionSvg from "$assets/question.svg"
  import { settings } from "$lib/settings"

  export let logoUrl: string
</script>

<div class="wrapper">
  <a href="/scan">
    <img class="left-arrow" src={LeftArrowSvg} alt="" aria-hidden="true" />
  </a>
  {#if logoUrl}
    <img class="question" src={logoUrl} alt="" aria-hidden="true" />
  {/if}
  <a href={settings.DOCUMENTATION_URL}>
    <img class="metadata" src={QuestionSvg} alt="" aria-hidden="true" />
  </a>
</div>

<style>
  .wrapper {
    height: 3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 0;
  }
  .left-arrow {
    height: 1.2rem;
  }
  .question {
    height: 2.5rem;
  }
  .metadata {
    height: 2rem;
  }
</style>
