<script lang="ts">
  /*
      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Machine/QualityMetrics_v0.1.py
  */

  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import TrueIcon from "$assets/true-circle.svg"
  import FalseIcon from "$assets/false-circle.svg"
  import Divider from "$components/Divider/index.svelte"

  export let data: {
    metrics: {
      serial: string
      name: string
      measurements: {
        name: string
        ok: boolean
        value: number
      }[]
    }[]
  }
</script>

<Article>
  {#each data.metrics as metric, i}
    <DataRow label="Name" value={metric.name} />
    <DataRow label="Serial number" value={metric.serial} />
    {#each metric.measurements as m}
      <div class="data">
        <div class="label">{m.name}:</div>
        <div class="value">
          <span>{m.value}</span>
          <div class="icon-wrapper">
            <img src={m.ok ? TrueIcon : FalseIcon} alt={m.ok ? "Passed" : "Didn't pass"} />
          </div>
        </div>
      </div>
    {/each}
    {#if i !== data.metrics.length - 1}
      <Divider />
    {/if}
  {/each}
</Article>

<style lang="scss">
  .data {
    display: flex;
    font-size: 1rem;
    font-style: normal;
    font-weight: 400;

    &:not(:last-child) {
      margin-bottom: 1rem;
    }
  }

  .label {
    flex: 0 0 45%;
    line-height: 150%;
    padding-right: 0.5rem;
  }

  .value {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    line-height: 150%;
    flex: 0 0 55%;
    word-break: break-word;

    .icon-wrapper {
      width: 1.25rem;
      display: flex;
    }
  }
</style>
