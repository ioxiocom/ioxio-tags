<script lang="ts">
  export let onClick: () => void
  export let icon: string | null = null
  export let title: string
  export let background: string = "#3CB08E"
  export let width: string = "100%"
  export let height: string = "auto"
  export let maxWidth: string = "10.6875rem"
</script>

<button
  class="button"
  on:click={onClick}
  style="--background:{background}; --width:{width}; --height:{height}; --maxWidth:{maxWidth};"
>
  {#if icon}
    <img class="icon" src={icon} alt="icon" />
  {/if}
  <span class="title">{title}</span>
</button>

<style lang="scss">
  .button {
    cursor: pointer;
    margin: auto;
    padding: 0.5rem 1rem;
    background-color: var(--background);
    border-radius: 0.3125rem;
    border: none;
    max-width: var(--maxWidth);
    width: var(--width);
    height: var(--height);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    @media screen and (max-height: 600px) {
      padding: 0.3rem 1rem;
    }
  }
  .button:active {
    opacity: 0.7;
  }
  .title {
    color: white;
    font-family: "Poppins" sans-serif;
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.5rem;
  }
</style>
