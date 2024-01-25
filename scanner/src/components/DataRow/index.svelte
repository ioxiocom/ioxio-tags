<script lang="ts">
  export let label: string
  export let value: string | string[]
</script>

<div class="row">
  <div class="label">
    {label}:
  </div>
  <div class="value">
    {#if typeof value === "string"}
      {value.trim() || "-"}
    {:else if value === null || value === undefined}
      -
    {:else if value.length === 0}
      <div>-</div>
    {:else}
      {#each value as v}
        <div>{v.trim() || "-"}</div>
      {/each}
    {/if}
  </div>
</div>

<style lang="scss">
  .row {
    display: flex;
    flex-direction: row;
    font-size: 1rem;
    font-style: normal;
    font-weight: 400;
    &:not(:last-child) {
      margin-bottom: 1rem;
    }
  }
  .label {
    flex: 0 0 45%;
    line-height: 1.5rem;
    padding-right: 0.5rem;
  }
  .value {
    line-height: 1.5rem;
    flex: 0 0 55%;
    word-break: break-word;
  }
</style>
