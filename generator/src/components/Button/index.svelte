<script lang="ts">
  export let onClick: () => void
  export let icon: string | null = null
  export let title: string
</script>

<button class="button" on:click|preventDefault={onClick}>
  {#if icon}
    <img class="icon" src={icon} alt="icon" />
  {/if}
  <span class="title">{title}</span>
</button>

<style>
  .button {
    cursor: pointer;
    padding: 1rem 1.5rem;
    background: rgba(15, 37, 67, 1);
    border-radius: 0.5rem;
    border: none;
    min-width: 8rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
  }
  .button:active {
    opacity: 0.7;
  }
  .title {
    color: white;
    font-size: 1.3rem;
  }
</style>
