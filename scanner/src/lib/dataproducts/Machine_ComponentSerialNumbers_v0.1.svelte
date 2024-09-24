<script lang="ts">
  /*
      https://github.com/ioxio-dataspace/sandbox-definitions/blob/main/src/DigitalProductPassport/Machine/ComponentSerialNumbers_v0.1.py
  */

  import DataRow from "$components/DataRow/index.svelte"
  import Article from "$components/Article/index.svelte"

  export let data: {
    serialNumbers: {
      name: string
      serial: string
    }[]
  }
</script>

<Article>
  {#each data.serialNumbers as sn}
    <DataRow label={sn.name} value={sn.serial} />
  {/each}
</Article>
