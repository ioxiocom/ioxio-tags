<script lang="ts">
  import type { components } from "$lib/openapi"
  import { supportedDataProducts } from "$lib/dataproducts"
  import ChevronLeftSvg from "$assets/chevron-left.svg"
  import LoadingSvg from "$assets/loading.svg"
  import { dataproduct } from "$lib/api"
  import { consoleLog } from "$lib/common"

  type SupportedDataproduct = components["schemas"]["SupportedDataproduct"]
  let productMetadata: SupportedDataproduct = {
    name: "Data Sheet For Metal Artifacts",
    description: "Returns the basic product information of a metal product",
    path: "DigitalProductPassport/MetalArtifact/DataSheet_v0.1",
    source: "dpp_demo",
  }
  let dataspace: string = "sandbox.ioxio-dataspace.com"
  let product: string = "177389-09633"
  let id: string = "steel-roll-1234b"

  let supported = productMetadata.path in supportedDataProducts
  console.log(`Supported: ${supported}`)
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
      console.log(params)
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

<div class="card">
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
  <div class="subtitle" class:divider={open}>{productMetadata.description}</div>
  {#if loadedData}
    <section>
      <svelte:component this={component} status={loadedStatus} data={loadedData} />
    </section>
  {/if}
</div>

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

  .card {
    background: #1a2934;
    border-radius: 0.5rem;
    padding: 1rem 0.5rem;
    font-weight: 400;
    line-height: 1.125rem;
    letter-spacing: 0em;
    margin-bottom: 1.5rem;

    .dataproduct-name {
      flex-grow: 1;
      color: white;
      font-size: 1rem;
    }

    .subtitle {
      font-size: 0.75rem;
      font-weight: 400;
      color: white;
    }

    .header {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1rem;
    }

    .divider {
      padding-bottom: 1rem;
      border-bottom: 1px solid #20303e;
      margin-bottom: 1rem;
    }
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
