<script lang="ts">
  import type { components } from "$lib/openapi"
  import ChevronLeftSvg from "$assets/chevron-left.svg"
  import { tag } from "$lib/api"

  type SupportedDataproduct = components["schemas"]["SupportedDataproduct"]

  export let productBrief: SupportedDataproduct
  export let dataspaceDomain: string
  export let product: string
  export let logoUrl: string

  let fetched: boolean = false
  let loading: boolean = false
  let data: any = null

  async function fetchProduct() {
    if (fetched) {
      fetched = false
      return
    }
    if (data) {
      fetched = true
      return
    }
    loading = true
    const result = await tag.fetchDataProduct({
      // Test Data for DataProduct Fetch
      dataspace_domain: "sandbox.ioxio-dataspace.com",
      product_path: "DPP/Energy/Battery/ProductDataSheet_v0.1",
      source: "dpp_demo",
      product: "MPP48V",
      // dataspace_domain: dataspaceDomain,
      // product_path: productBrief.path,
      // source: productBrief.source,
      // product,
      id: "test",
    }).result
    if (result.ok) {
      data = result.data
      fetched = true
    } else {
      // TODO: Better error handling
      console.error("DataProduct fetching failed", result)
      fetched = false
    }
    loading = false
  }
</script>

<div class="card">
  <div class="header" class:divider={fetched}>
    <div>
      <div class="dataproduct-name">{productBrief.name}</div>
      <div class="subtitle">{productBrief.description}</div>
    </div>
    <button class="button" class:fetch={!fetched} class:close={fetched} on:click={fetchProduct}>
      {#if loading}
        Fetching
      {:else}
        <span>{fetched ? "Close" : "Fetch"}</span>
        <img src={ChevronLeftSvg} alt="" aria-hidden="true" />
      {/if}
    </button>
  </div>
  {#if fetched}
    <div class="information">
      {#each Object.keys(data).filter((key) => !key.includes("svelte")) as key}
        <div class="row">
          <div class="property capitalize">{key.replace(/([a-z])([A-Z])/g, "$1 $2")}:</div>
          <div class="value">
            {#if data[key] instanceof Array}
              {#each data[key] as value}
                <div class="item">{value}</div>
              {/each}
            {:else if typeof data[key] === "object"}
              {#each Object.keys(data[key]) as nestKey}
                <div class="item">
                  <span class="capitalize">{nestKey.replace(/([a-z])([A-Z])/g, "$1 $2")}</span>
                  {data[key][nestKey]}
                </div>
              {/each}
            {:else}
              {#if key === "manufacturer"}
                <div class="item">
                  <img class="manufacturer" src={logoUrl} alt="" aria-hidden="true" />
                </div>
              {/if}
              <div class="item">
                {data[key]}
              </div>
            {/if}
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style lang="scss">
  .card {
    background: #1a2934;
    border-radius: 0.5rem;
    padding: 1rem 0.5rem;
    font-size: 0.75rem;
    font-weight: 400;
    line-height: 1.125rem;
    letter-spacing: 0em;
    margin-bottom: 1rem;
    .basic-information {
      color: #798893;
      margin-bottom: 1rem;
    }
    .dataproduct-name {
      color: white;
      font-size: 1rem;
      margin-bottom: 1rem;
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
    }
    .divider {
      padding-bottom: 0.5rem;
      border-bottom: 1px solid #20303e;
      margin-bottom: 1rem;
    }
  }
  .row {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    color: white;
    &:not(:last-child) {
      margin-bottom: 1rem;
    }
    .property {
      font-size: 0.75rem;
      font-weight: 400;
      flex: 0 0 40%;
      padding-right: 0.5rem;
    }
    .value {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      .item {
        &:not(:last-child) {
          margin-bottom: 0.5rem;
        }
      }
    }
  }
  .capitalize {
    text-transform: capitalize;
  }
  .flex-item {
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .trusted {
    margin-left: 0.5rem;
    color: #3cb08e;
  }
  .button {
    color: white;
    font-size: 0.75rem;
    font-weight: 600;
    text-align: center;
    border-radius: 0.3rem;
    border: none;
    color: white;
    width: 5.625rem;
    padding: 0.5rem 0.25rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.25rem;
    &.fetch {
      background-color: #3cb08e;
    }
    &.close {
      background: #101920;
      img {
        transform: rotate(90deg);
      }
    }
    &.unsupport {
      background-color: #20303e;
    }
  }
  .manufacturer {
    height: 2rem;
  }
</style>
