<script context="module" lang="ts">
</script>

<script lang="ts">
  export let options: string[] = []
  export let value: string
</script>

<div class="wrapper">
  {#each options as option, i}
    <button
      class="toggle-item"
      class:active={value && value === option}
      on:click={() => value = option}
    >
      {option}
    </button>
  {/each}
</div>

<style lang="scss">
  .wrapper {
    display: flex;
    flex-direction: row;
    align-items: center;
    .toggle-item {
      border: none;
      width: 8rem;
      height: 2.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(238, 239, 236, 1);
      color: rgba(16, 25, 32, 1);
      cursor: pointer;
      &.active {
        background: rgba(16, 25, 32, 1);
        color: white;
      }
      &:first-child {
        border-top-left-radius: 0.3rem;
        border-bottom-left-radius: 0.3rem;
      }
      &:last-child {
        border-top-right-radius: 0.3rem;
        border-bottom-right-radius: 0.3rem;
      }
    }
  }
</style>
