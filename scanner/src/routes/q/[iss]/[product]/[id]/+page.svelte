<script lang="ts">
  import Header from "$components/Header/index.svelte"
  import Footer from "$components/Footer/index.svelte"
  import BatteryPng from "$assets/battery.png"
  import GreenCheckSvg from "$assets/green-check.svg"
  import ChevronLeftSvg from "$assets/chevron-left.svg"
  import { onMount } from "svelte"
  import { page } from "$app/stores"

  let data: any = {}
  let availableProductFetched: boolean = false
  let secondProductFetched: boolean = false

  onMount(async () => {
    data = history.state
    console.log(data)
  })
</script>

<Header />
<div class="content">
  <div class="logo-title">
    <div class="logo"><img src={BatteryPng} alt="" aria-hidden="true" /></div>
    <div class="title">{data.name}</div>
  </div>
  <div class="card">
    <div class="basic-information">BASIC INFORMATION</div>
    <div class="row">
      <div class="property">Verification state:</div>
      <div class="value">
        <div class="flex-item">
          <img src={GreenCheckSvg} alt="" aria-hidden="true" />
          <span class:trusted={true}>Trusted</span>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="property">product Code:</div>
      <div class="value">{data.product}</div>
    </div>
    <div class="row">
      <div class="property capitalize">Dataspace domain:</div>
      <div class="value">{$page.params.iss}</div>
    </div>
  </div>
  <div class="card">
    <div class="header" class:divider={availableProductFetched}>
      <div>
        <div class="dataproduct-name">Available Dataproduct name</div>
        <div class="subtitle">Data product description</div>
      </div>
      <button
        class="button"
        class:fetch={!availableProductFetched}
        class:close={availableProductFetched}
        on:click={() => (availableProductFetched = !availableProductFetched)}
      >
        <span>{availableProductFetched ? "Close" : "Fetch"}</span>
        <img src={ChevronLeftSvg} alt="" aria-hidden="true" />
      </button>
    </div>
    {#if availableProductFetched}
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
                {data[key]}
              {/if}
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
  <div class="card">
    <div class="header">
      <div>
        <div class="dataproduct-name">Second Dataproduct name</div>
        <div class="subtitle">Data product description</div>
      </div>
      <button class="button unsupport" on:click={() => alert("unsupported")}>Unsupported</button>
    </div>
    {#if secondProductFetched}
      <div class="information" />
    {/if}
  </div>
</div>
<Footer />

<style lang="scss">
  .content {
    flex: 1;
    padding: 1rem 0;
    overflow-y: auto;
  }
  .logo-title {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1rem;
    .logo {
      width: 5rem;
      height: 5rem;
      background: #e1e1e1;
      border-radius: 0.5rem;
      display: flex;
      align-items: center;
      justify-content: center;
      img {
        width: 100%;
        height: auto;
      }
    }
    .title {
      color: white;
      font-size: 1.125rem;
      font-weight: 600;
      line-height: 1.68rem;
    }
  }
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
</style>
