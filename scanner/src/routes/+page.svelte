<script lang="ts">
  import IoxioTagLogo from "$assets/ioxio-tag-logo.svg"
  import Camera from "$assets/camera.svg"
  import Subtract from "$assets/subtract.svg"
  import Button from "$components/Button/index.svelte"
  import { goto } from "$app/navigation"
</script>

<div class="container">
  <div class="background" />
  <div class="relative barcode-scanner-area-wrapper">
    <div class="relative barcode-scanner-area">
      <img alt="subtract" class="subtract-image" src={Subtract} />
        <img class="logo" src={IoxioTagLogo} alt="logo" />
    </div>
    <div>
      <div class="relative">
          <p class="description">
            Turn on your camera for scan a Product Passport QR code to view product data
          </p>
      </div>
      <div class="relative button-wrapper">
        <Button onClick={() => goto("/scan")} icon={Camera} title="Turn on" />
      </div>
    </div>
  </div>
</div>

<style>
  .background {
    background: rgba(16, 25, 32, 1);
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
  }
  .barcode-scanner-area-wrapper {
    flex: 1;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 1rem;
    margin: auto;
  }
  .barcode-scanner-area {
    display: flex;
    justify-content: center;
    width: fit-content;
    margin-left: auto;
    margin-right: auto;
  }
  .subtract-image {
    position: relative;
    width: auto;
    z-index: 1;
    max-height: 40vh;
  }
  @media screen and (max-width: 520px) {
    .subtract-image {
      width: 100%;
    }
  }
  .description {
    text-align: center;
    font-size: 1rem;
    color: white;
    margin-top: 3rem;
  }
  .button-wrapper {
    display: flex;
    justify-content: center;
    margin-top: 2rem;
  }
  .logo {
    width: 80%;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
</style>
