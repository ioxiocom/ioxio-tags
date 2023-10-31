<script lang="ts">
  import Header from "$components/Header/index.svelte"
  import Footer from "$components/Footer/index.svelte"
  import Loading from "$components/Loading/index.svelte"
  import BasicInformation from "$components/BasicInformation/index.svelte"
  import DataProduct from "$components/DataProduct/index.svelte"
  import { page } from "$app/stores"
  import queryString from "query-string"
  import { onDestroy, onMount } from "svelte"
  import type { components } from "$lib/openapi"
  import { tag } from "$lib/api"
  import ErrorSvg from "$assets/error.svg"
  import { goto } from "$app/navigation"
  import { App } from "@capacitor/app"

  let loading: boolean = false
  let meta: components["schemas"]["MetadataV1Response"] | undefined = undefined
  let verifiedParam = queryString.parse($page.url.search).verified
  let verified = verifiedParam === "true" ? true : verifiedParam === "false" ? false : undefined
  let error: string

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
      error =
        result.data.detail && result.data.detail.length > 0
          ? result.data.detail[0].msg
          : result.data.error

      setTimeout(() => {
        rescan()
      }, 2000)
    }
    loading = false
  }

  function rescan() {
    goto("/scan")
  }

  onMount(() => {
    load()
    if (typeof document !== "undefined") {
      App.addListener("backButton", function (e) {
        goto("/")
      })
    }
  })

  onDestroy(() => {
    App.removeAllListeners()
  })
</script>

{#if loading}
  <div class="loader">
    <Loading type="light" />
  </div>
{:else if meta}
  <div class="content">
    <Header logoUrl={meta.logo_url} />
    <BasicInformation {meta} product={$page.params.product} {verified} />
    {#each meta.supported_dataproducts as dataProduct}
      <DataProduct productBrief={dataProduct} />
    {/each}
  </div>
  <Footer />
{:else}
  <div class="relative failed-verification-wrapper">
    <img src={ErrorSvg} alt="" aria-hidden="true" />
    <p>{error}</p>
  </div>
  <div class="actions-wrapper">
    <p>Returning to scanning mode...</p>
  </div>
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
  }
  .failed-verification-wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 3.1875rem;
    margin: auto;
    @media screen and (max-height: 600px) {
      padding: 0.5rem 0;
    }
    img {
      width: 5rem;
      height: 5rem;
    }
    p {
      color: #eeefec;
      text-align: center;
      font-size: 1rem;
      font-style: normal;
      font-weight: 400;
      line-height: 150%; /* 24px */
      padding: 0 1rem;
    }
  }
  .actions-wrapper {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 0.875rem;
    p {
      display: block;
      color: white;
      font-size: 0.8rem;
      text-align: center;
    }
  }
</style>
