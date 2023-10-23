<script>
  import "./styles.css"
  import LogomarkSvg from "$assets/ioxio-logomark.svg?url"
</script>

<div class="app">
  <main>
    <img class="logomarkSvg" src={LogomarkSvg} alt="" aria-hidden="true" />
    <slot />
  </main>
</div>

<style lang="scss">
  .app {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  main {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  .logomarkSvg {
    width: 20%;
    position: absolute;
    bottom: -1.8125rem;
    left: -2%;
    z-index: 0;
    @media screen and (max-width: 90rem) {
      display: none;
    }
  }
</style>
