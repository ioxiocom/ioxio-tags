<script lang="ts">
  import type { components } from "$lib/openapi"
  import ChevronLeftSvg from "$assets/chevron-left.svg"

  let fetched: boolean = false
  type SupportedDataproduct = components["schemas"]["SupportedDataproduct"]
  export let productBrief: SupportedDataproduct

  function onFetch() {
    // TODO: implement fetch dataProduct later
    fetched = !fetched
  }
</script>

<div class="card">
  <div class="header" class:divider={fetched}>
    <div>
      <div class="dataproduct-name">{productBrief.name}</div>
      <div class="subtitle">{productBrief.description}</div>
    </div>
    <button class="button" class:fetch={!fetched} class:close={fetched} on:click={onFetch}>
      <span>{fetched ? "Close" : "Fetch"}</span>
      <img src={ChevronLeftSvg} alt="" aria-hidden="true" />
    </button>
  </div>
</div>

<style lang="scss">
  .card {
    background: #1a2934;
    border-radius: 0.5rem;
    padding: 1rem 0.5rem;
    font-weight: 400;
    line-height: 1.125rem;
    letter-spacing: 0em;
    margin-bottom: 1rem;
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
      gap: 1rem;
    }
    .divider {
      padding-bottom: 0.5rem;
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
    color: white;
    width: 5.625rem;
    flex: 0 0 5.625rem;
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
