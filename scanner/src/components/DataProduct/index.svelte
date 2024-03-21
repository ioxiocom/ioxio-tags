<script lang="ts">
  import type { components } from "$lib/openapi"
  import { supportedDataProducts } from "$lib/dataproducts"
  import ChevronLeftSvg from "$assets/chevron-left.svg"
  import LoadingSvg from "$assets/loading.svg"
  import { dataproduct } from "$lib/api"
  import { consoleLog } from "$lib/common"

  import Card from "$components/Common/Card/index.svelte"
  import Subtitle from "$components/Common/Subtitle/index.svelte"

  type SupportedDataproduct = components["schemas"]["SupportedDataproduct"]
  export let productMetadata: SupportedDataproduct
  export let dataspace: string
  export let product: string
  export let id: string

  let supported = productMetadata.path in supportedDataProducts

  let open: boolean = false
  let loading = false

  let loadedStatus = undefined
  let loadedData = undefined
  let component = supportedDataProducts[productMetadata.path]

  async function onButtonClick() {
    try {
      if (open) {
        loadedData = undefined
        loadedStatus = undefined
        open = false
        loading = false
        return
      }

      loading = true

      const params = {
        dataspace_domain: dataspace,
        product_path: productMetadata.path,
        source: productMetadata.source,
        product: product,
        id: id,
      }

      const req = dataproduct.fetch(params)
      const result = await req.result

      if (result.ok) {
        loadedStatus = result.status
        loadedData = result.data
        open = true
      } else {
        let error = "Unknown error"
        if (result.data.detail && result.data.detail[0].msg) {
          error = result.data.detail[0].msg
        } else if (result.data.detail) {
          error = result.data.detail
        } else if (result.data.message) {
          error = result.data.message
        }
        consoleLog(`Error fetching: ${error}`)
      }
    } catch (error: any) {
      consoleLog(`Error fetching: ${error}`)
    } finally {
      loading = false
    }
  }
</script>

<Card>
  <div class="header">
    <div class="dataproduct-name">{productMetadata.name}</div>
    {#if supported}
      <button class="button" class:fetch={!open} class:close={open} on:click={onButtonClick}>
        <span>{open ? "Close" : "Fetch"}</span>
        {#if loading}
          <img class="loading" src={LoadingSvg} alt="" aria-hidden="true" />
        {:else}
          <img src={ChevronLeftSvg} alt="" aria-hidden="true" />
        {/if}
      </button>
    {:else}
      <button class="button unsupported" disabled> Unsupported </button>
    {/if}
  </div>
  {#if loadedData}
    <Subtitle noBottomMargin showDivider={open}>{productMetadata.description}</Subtitle>
    <section>
      <svelte:component this={component} status={loadedStatus} data={loadedData} />
    </section>
  {/if}
</Card>

<style lang="scss">
  @mixin keyframes($name) {
    @keyframes #{$name} {
      @content;
    }
  }

  @include keyframes(loading) {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  .dataproduct-name {
    flex-grow: 1;
    color: white;
    font-size: 1rem;
    line-height: 150%;
  }
  .header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
  }

  .button {
    color: white;
    font-size: 1rem;
    font-weight: 600;
    text-align: center;
    border-radius: 0.3rem;
    border: none;
    flex-shrink: 0;
    width: 5.625rem;
    padding: 0.5rem 0.25rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
    cursor: pointer;

    &.fetch {
      background-color: #3cb08e;
    }

    &.close {
      background: #101920;

      img {
        transform: rotate(-90deg);
      }
    }

    img {
      height: 1rem;
      width: 1rem;

      &.loading {
        animation: loading 1s linear infinite;
      }
    }

    &.unsupported {
      border-radius: 3px;
      background-color: #20303e;
      font-size: 12px;
      font-style: normal;
      font-weight: 400;
      line-height: 150%; /* 18px */
      cursor: not-allowed;
    }
  }
</style>
