<script lang="ts">
  export let onClick: (() => void) | undefined = undefined
  export let icon: string | undefined = undefined
  export let title: string
  export let disabled: boolean = false
  export let type: "button" | "submit" | "reset" = "button"

  function onClickHandler() {
    if (disabled) {
      return
    }
    if (onClick) {
      onClick()
    }
  }
</script>

<button class="button" on:click={onClickHandler} class:disabled {type}>
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
  img {
    z-index: 2;
    margin-right: 0.5rem;
  }
  .title {
    color: white;
    font-size: 1.3rem;
    position: relative;
    z-index: 2;
  }
</style>
