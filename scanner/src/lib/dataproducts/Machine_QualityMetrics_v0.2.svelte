<script lang="ts">
  /*
      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Machine/QualityMetrics_v0.2.py
  */

  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"
  import TrueIcon from "$assets/true-circle.svg"
  import FalseIcon from "$assets/false-circle.svg"
  import Divider from "$components/Divider/index.svelte"

  export let data: {
    metrics: {
      identification: string
      serial: string
      name: string
      measurements: {
        name: string
        ok: boolean
        targetDeviation: string
        cp: number
        cpk: number
        pp: number
        ppk: number
      }[]
    }[]
  }
</script>

<Article>
  {#each data.metrics as metric, i}
    <DataRow label="Identification" value={metric.identification} />
    <DataRow label="Serial number" value={metric.serial} />
    <DataRow label="Name" value={metric.name} />
    {#each metric.measurements as m}
      <Divider />
      <div class="data">
        <div class="label">{m.name}:</div>
        <div class="value">
          <div class="icon-wrapper">
            <img src={m.ok ? TrueIcon : FalseIcon} alt={m.ok ? "Passed" : "Didn't pass"} />
          </div>
        </div>
      </div>
      <div class="data">
        <div class="label">Deviation:</div>
        <div class="value">
          {m.targetDeviation}
        </div>
      </div>
      <div class="grid">
        <div>Cp</div>
        <div>Cpk</div>
        <div>Pp</div>
        <div>Ppk</div>
        <div>{m.cp}</div>
        <div>{m.cpk}</div>
        <div>{m.pp}</div>
        <div>{m.ppk}</div>
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
    line-height: 150%;
    padding-right: 0.5rem;
  }

  .value {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    line-height: 150%;
    word-break: break-word;

    .icon-wrapper {
      width: 1.25rem;
      display: flex;
    }
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    margin-bottom: 1rem;
    max-width: 30rem;
  }
</style>
