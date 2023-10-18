<script lang="ts">
  export let onClick: () => void
  export let icon: string | null = null
  export let title: string
</script>

<button class="button" on:click={onClick}>
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
    background-color: rgba(60, 176, 142, 1);
    border-radius: 0.5rem;
    border: none;
    min-width: 8rem;
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
