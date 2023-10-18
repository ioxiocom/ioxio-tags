<script lang="ts">
  import LoadingScroller from "$assets/loading-scroller.gif"
  import LoadingXOverlayDark from "$assets/loading-x-overlay-dark.svg?url"
  import LoadingXOverlayLight from "$assets/loading-x-overlay-light.svg?url"

  export let type: "dark" | "light"

  const LoadingXOverlay = type === "dark" ? LoadingXOverlayDark : LoadingXOverlayLight
</script>

<div class="loading">
  <img class="scroller" src={LoadingScroller} alt="Loading" />
  <img class="overlay" src={LoadingXOverlay} alt="" aria-hidden="true" />
</div>

<style lang="scss">
  $height: 48px;
  .loading {
    margin: 1rem auto;
    position: relative;
    width: 100%;
    display: flex;
    justify-content: center;

    .scroller {
      height: $height;
    }
    .overlay {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translate(-50%, 0);
      height: $height;
    }

    &:before {
      box-shadow: -15px 0 15px -15px inset;
      left: -15px;
    }

    &:after {
      box-shadow: 15px 0 15px -15px inset;
      right: -15px;
    }
  }
</style>
