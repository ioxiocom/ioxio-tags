<script lang="ts">
  export let label: string
  export let value: string | string[]
  export let link: boolean = false
  export let column: boolean = false
</script>

<div class={`data ${column ? "column" : "row"}`}>
  <div class="label">
    {label}:
  </div>
  {#if link || (typeof value === "string" && value.startsWith("https://"))}
    <div class="value">
      {#if typeof value === "string"}
        <a href={value} target="_blank" rel="noreferrer">{value}</a>
      {:else if value === null || value === undefined || value.length === 0}
        -
      {:else}
        {#each value as v}
          <a href={v} target="_blank" rel="noreferrer">{v}</a>
        {/each}
      {/if}
    </div>
  {:else}
    <div class="value">
      {#if typeof value === "string"}
        {value.trim() || "-"}
      {:else if value === null || value === undefined || value.length === 0}
        -
      {:else}
        {#each value as v}
          <div>{v.trim() || "-"}</div>
        {/each}
      {/if}
    </div>
  {/if}
</div>

<style lang="scss">
  .data {
    display: flex;
    font-size: 1rem;
    font-style: normal;
    font-weight: 400;

    &:not(:last-child) {
      margin-bottom: 1rem;
    }

    &.row {
      flex-direction: row;
      align-items: center;
    }

    &.column {
      flex-direction: column;
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

    a {
      color: #3cb08e;
    }
  }
</style>
