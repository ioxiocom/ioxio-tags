<script lang="ts">
  import Header from "$components/Header/index.svelte"
  import Footer from "$components/Footer/index.svelte"
  import Loading from "$components/Loading/index.svelte"
  import BasicInformation from "$components/BasicInformation/index.svelte"
  import DataProduct from "$components/DataProduct/index.svelte"
  import { page } from "$app/stores"
  import { tag } from "$lib/api"

  let loading: boolean
  let meta: any = null

  async function load() {
    loading = true
    console.log($page.params)
    const result = await tag.fetchMetaDataV1({
      iss: $page.params.iss,
      product: $page.params.product,
    }).result

    if (result.ok) {
      meta = result.data
      console.log(meta)
    } else {
      console.error("Generating tag failed", result)
      meta = null
    }
    loading = false
  }
  load()
</script>

{#if Boolean(loading)}
  <div class="loader">
    <Loading type="light" />
  </div>
{:else}
  <Header logoUrl={meta?.logo_url} />
  <div class="content">
    {#if meta}
      <BasicInformation {meta} product={$page.params.product} />
      {#each meta.supported_dataproducts as dataProduct}
        <DataProduct
          productBrief={dataProduct}
          dataspaceDomain={meta.product_dataspace}
          product={$page.params.product}
          logoUrl={meta.logo_url}
        />
      {/each}
    {:else}
      Error
    {/if}
  </div>
  <Footer />
{/if}

<style lang="scss">
  .loader {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .content {
    flex: 1;
    padding: 1rem 0;
    overflow-y: auto;
  }
</style>
