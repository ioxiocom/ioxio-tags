<script lang="ts">
  import Question from "$assets/question.svg"
</script>

<a class="relative documentation-wrapper" href="/">
  <img alt="question" src={Question} />
  <p class="documentation-label">Documentation</p>
</a>

<style>
  .documentation-wrapper {
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 1rem;
    font-weight: 600;
    line-height: 1.5rem;
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
