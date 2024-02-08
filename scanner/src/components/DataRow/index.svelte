<script lang="ts">
  export let label: string
  export let value: string | string[]
  export let link: boolean = false
</script>

<div class="row">
  <div class="label">
    {label}:
  </div>
  {#if link || (typeof value === "string" && value.startsWith("https://"))}
    <div class="value">
      {#if typeof value === "string"}
        <a class="link" href={value} target="_blank" rel="noreferrer">{value}</a>
      {:else if value === null || value === undefined || value.length === 0}
        -
      {:else}
        {#each value as v}
          <a class="link" href={v} target="_blank" rel="noreferrer">{v}</a>
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

    .link {
      color: #3cb08e;
    }
  }
</style>
