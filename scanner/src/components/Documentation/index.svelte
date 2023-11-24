<script lang="ts">
  import Question from "$assets/question.svg"
  import { settings } from "$lib/settings"
</script>

<a class="wrapper" href={settings.DOCUMENTATION_URL} target="_blank" rel="noreferrer">
  <img alt="question" src={Question} />
  <span class="label">Documentation</span>
</a>

<style lang="scss">
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
    z-index: 1;
    @media screen and (max-height: 600px) {
      margin-top: 0.2rem;
    }
  }

  img {
    width: 2rem;
    @media screen and (max-height: 600px) {
      width: 1.2rem;
    }
  }

  .label {
    color: white;
    font-size: 1.2rem;
    @media screen and (max-height: 600px) {
      font-size: 0.8rem;
    }
  }
</style>
