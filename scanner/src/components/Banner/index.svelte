<script lang="ts">
  import SvLogo from "$assets/sv-logo.svg?raw"

  export let iss: string
  export let product: string
  export let id: string
</script>

{#if product === "BG01844196" && id === "minexpo-demo-1"}
  <div class="wrapper sv">
    <div class="logo-wrapper">
      {@html SvLogo}
    </div>
    <a href="https://www.rocktechnology.sandvik/bevdrills" rel="noopener noreferrer" target="_blank"
      >Get more information</a
    >
  </div>
{/if}

<style lang="scss">
  .wrapper {
    border-radius: 5px;
    margin-bottom: 1rem;

    &.sv {
      background-color: #fff;
      display: flex;
      justify-content: space-between;
      padding: 1rem;
      gap: 1rem;
      align-items: center;

      .logo-wrapper {
        height: 2rem;
      }

      :global(svg) {
        width: 100%;
        height: 100%;
      }

      a {
        font-family: "Roboto Condensed", system-ui;
        font-weight: 400;
        background-color: #e6e6e6;
        padding: 1rem;
        color: #000;
        text-decoration: none;
        flex-shrink: 0;
      }
    }
  }
</style>
