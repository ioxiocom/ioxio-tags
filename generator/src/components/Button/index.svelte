<script lang="ts">
  export let onClick: () => void
  export let icon: string | null = null
  export let title: string
  export let disabled: boolean = false

  function onClickHandler() {
    if (disabled) return
    onClick()
  }
</script>

<button class="button" on:click|preventDefault={onClickHandler} class:disabled>
  {#if icon}
    <img class="icon" src={icon} alt="icon" />
  {/if}
  <span class="title">{title}</span>
</button>

<style lang="scss">
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
  .disabled {
    cursor: not-allowed;
    background-color: #d9d9d9;
    & > .title {
      color: #828282;
    }
  }
  .button:not(.disabled):active {
    opacity: 0.7;
  }
  .title {
    color: white;
    font-size: 1.3rem;
  }
</style>
