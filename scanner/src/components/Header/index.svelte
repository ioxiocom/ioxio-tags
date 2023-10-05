<script lang="ts">
  import LeftArrowSvg from "$assets/left-arrow.svg"
  import QuestionSvg from "$assets/question.svg"
  import MetaDataPng from "$assets/metadata.png"
</script>

<div class="wrapper">
  <a href="/">
    <img class="left-arrow" src={LeftArrowSvg} alt="" aria-hidden="true" />
  </a>
  <img class="question" src={MetaDataPng} alt="" aria-hidden="true" />
  <a href="/">
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
