<script>
  import "./styles.css"
</script>

<div class="app">
  <main>
    <slot />
  </main>
</div>

<style>
  .app {
    display: flex;
    flex-direction: column;
  }

  main {
    display: flex;
    flex-direction: column;
    background: black;
    min-height: 100vh;
  }
</style>
