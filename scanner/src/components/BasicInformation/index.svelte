<script lang="ts">
  import type { components } from "$lib/openapi"
  import VerificationSuccessSvg from "$assets/verification-success.svg"
  import VerificationFailedSvg from "$assets/verification-failed.svg"

  type MetadataV1Response = components["schemas"]["MetadataV1Response"]

  export let meta: MetadataV1Response
  export let product: string
  export let verified: boolean
</script>

<div class="logo-title">
  <div class="logo"><img src={meta.image_url} alt="" aria-hidden="true" /></div>
  <div class="title">{meta.names.en_US}</div>
</div>
<div class="card">
  <div class="basic-information">Basic Information</div>
  <div class="row">
    <div class="property">Verification state:</div>
    <div class="value">
      <div class="flex-item">
        {#if verified}
          <img src={VerificationSuccessSvg} alt="" aria-hidden="true" />
          <span class="status" class:trusted={true}>Trusted</span>
        {:else}
          <img src={VerificationFailedSvg} alt="" aria-hidden="true" />
          <span class="status" class:failed={true}>Verification failed</span>
        {/if}
      </div>
    </div>
  </div>
  <div class="row">
    <div class="property">Product Code:</div>
    <div class="value">{product}</div>
  </div>
  <div class="row">
    <div class="property capitalize">Dataspace domain:</div>
    <div class="value">{meta.product_dataspace}</div>
  </div>
</div>

<style lang="scss">
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
    }
    .status {
      font-size: 12px;
      font-style: normal;
      font-weight: 600;
      line-height: 150%; /* 18px */
    }
    .trusted {
      color: #3cb08e;
    }
    .failed {
      color: #dd596a;
    }
    .flex-item {
      display: flex;
      flex-direction: row;
      gap: 0.3rem;
      align-items: center;
    }
  }
</style>