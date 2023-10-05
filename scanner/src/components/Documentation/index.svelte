<script lang="ts">
  import Question from "$assets/question.svg"
  import { settings } from "$lib/settings"
</script>

<a class="wrapper" href={settings.DOCUMENTATION_URL}>
  <img alt="question" src={Question} />
  <span class="label">Documentation</span>
</a>

<style>
  .wrapper {
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 1rem;
    font-weight: 600;
    line-height: 1.5rem;
    gap: 0.5rem;
    position: relative;
  }

  img {
    width: 2rem;
  }

  .label {
    color: white;
    font-size: 1.2rem;
  }
</style>
