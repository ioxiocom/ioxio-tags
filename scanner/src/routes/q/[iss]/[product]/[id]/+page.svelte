<script lang="ts">
  import Header from "$components/Header/index.svelte"
  import Footer from "$components/Footer/index.svelte"
  import Loading from "$components/Loading/index.svelte"
  import BasicInformation from "$components/BasicInformation/index.svelte"
  import DataProduct from "$components/DataProduct/index.svelte"
  import { page } from "$app/stores"
  import queryString from "query-string"
  import { onMount } from "svelte"
  import type { components } from "$lib/openapi"
  import { tag } from "$lib/api"

  let loading: boolean = false
  let meta: components["schemas"]["MetadataV1Response"] | undefined = undefined
  let verified: boolean = queryString.parse($page.url.search).verified === "true"

  async function load() {
    loading = true
    const result = await tag.fetchMetaDataV1({
      iss: $page.params.iss,
      product: $page.params.product,
    }).result

    if (result.ok) {
      meta = result.data
    } else {
      console.error("Fetching metadata failed", result)
      meta = undefined
    }
    loading = false
  }
  onMount(() => {
    load()
  })
</script>

{#if loading || !meta}
  <div class="loader">
    <Loading type="light" />
  </div>
{:else}
  <div class="content">
    <Header logoUrl={meta.logo_url} />
    <BasicInformation {meta} product={$page.params.product} {verified} />
    {#each meta.supported_dataproducts as dataProduct}
      <DataProduct productBrief={dataProduct} />
    {/each}
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
