<script lang="ts">
  import type { Option } from "$components/FormSelectGroup/index.svelte"
  import FormInputGroup from "$components/FormInputGroup/index.svelte"
  import FormSelectGroup from "$components/FormSelectGroup/index.svelte"
  import FormCheckbox from "$components/FormCheckbox/index.svelte"
  import Button from "$components/Button/index.svelte"
  import Toggle from "$components/Toggle/index.svelte"
  import logoTagsSvg from "$assets/ioxio-tags-logo.svg"
  import effectSvg from "$assets/effect.svg"
  import logomarkSvg from "$assets/ioxio-logomark.svg"
  import logoSvg from "$assets/ioxio-logo.svg"
  import subtractSvg from "$assets/subtract.png"
  import type { PageData } from "./$types"

  export let data: PageData

  let productOption: Option
  const onToggleProduct = (option: Option) => {
    productOption = option
  }

  let signOption: Option
  const onToggleSign = (option: Option) => {
    signOption = option
  }
</script>

<svelte:head>
  <title>Generator</title>
  <meta name="description" content="QRcode Generator" />
</svelte:head>

<div class="container">
  <!-- Left Panel -->
  <div class="form-wrapper">
    <div class="title">Generate a product passport</div>
    <img class="logomarkSvg" src={logomarkSvg} alt="" />
    <form>
      <div class="row">
        <FormInputGroup name="domain" label="Issuer domain" placeholder="ex.tags.ioxio.dev" />
      </div>
      <div class="row">
        <div class="toggle-row">
          <Toggle options={data.productOptions} onToggle={onToggleProduct} value={productOption} />
        </div>
        <FormSelectGroup
          name="product"
          label="Product"
          placeholder="Type a product"
          options={data.options}
        />
      </div>
      <div class="row">
        <FormInputGroup name="productId" label="Product ID" placeholder="ex. VV123456-12" />
        <div class="toggle-row">
          <Toggle options={data.signOptions} onToggle={onToggleSign} value={signOption} />
        </div>
      </div>
      <div class="row">
        <FormCheckbox name="valid" label="Create valid signature" />
      </div>
      <div class="actions-wrapper">
        <Button title="Generate IOXIO Tag" onClick={() => {}} />
      </div>
    </form>
  </div>
  <!-- Right Panel -->
  <div class="qrcode-area-wrapper">
    <div class="qrcode-area">
      <div class="qrcode">
        <img class="frame" src={subtractSvg} alt="" />
        <img class="effect" src={effectSvg} alt="" />
        <img class="logo" src={logoTagsSvg} alt="" />
      </div>
    </div>
    <div class="status">IOXIO Tag generator</div>
    <div class="product-area">
      <div class="description">
        <div>
          This application serves as a demonstration platform for generating QR codes specifically
          designed for Data Product Passports.<br />Utilizing the IOXIO Dataspace technology, this
          app showcases how QR codes can be generated to serve as digital passports for various Data
          Products. These QR codes can be read using a compatible reader application, enabling
          access to relevant product details in real time.
        </div>
        <a class="documentation" href="/">See documentation →</a>
      </div>
    </div>
    <div class="footer">
      <span>Made by</span>
      <img src={logoSvg} alt="" />
    </div>
  </div>
</div>

<style lang="scss">
  .container {
    max-width: 1440px;
    display: flex;
    flex-direction: row;
    margin: auto;
    width: 100%;
    overflow: hidden;
    .form-wrapper {
      padding: 120px;
      background-color: white;
      width: 52%;
      position: relative;
      @media screen and (max-width: 1440px) {
        flex: 1;
        padding: 50px;
      }
      @media screen and (max-width: 1000px) {
        width: 100%;
      }
      .title {
        color: rgba(16, 25, 32, 1);
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 4rem;
      }
      form {
        position: relative;
      }
      .actions-wrapper {
        margin-top: 5rem;
      }
      .logomarkSvg {
        width: 30%;
        position: absolute;
        bottom: 0;
        left: -2%;
        z-index: 0;
      }
    }
    .qrcode-area-wrapper {
      padding: 100px 50px 20px;
      background-color: #111920;
      width: 48%;
      display: flex;
      flex-direction: column;
      @media screen and (max-width: 1440px) {
        flex: 1;
        padding: 50px;
      }
      @media screen and (max-width: 1000px) {
        width: 100%;
      }
      .qrcode-area {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        min-height: 420px;
        padding-bottom: 5rem;
        .frame {
          width: 300px;
          height: 300px;
          position: absolute;
          left: -25px;
          top: -25px;
        }
        .qrcode {
          width: 250px;
          height: 250px;
          position: relative;
        }
        .effect {
          position: absolute;
          left: 50%;
          top: 50%;
          transform: translate(-50%, -50%) rotate(-45deg);
          width: 140%;
        }
        .logo {
          position: absolute;
          left: 50%;
          top: 50%;
          transform: translate(-50%, -50%);
          width: 100%;
        }
      }
      .status {
        color: white;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        padding: 1rem 0;
      }
      .product-area {
        flex: 1;
        margin-bottom: 5rem;
        .description {
          text-align: center;
          color: white;
          font-size: 1.2rem;
          .documentation {
            margin-top: 2rem;
            display: block;
            color: rgba(60, 176, 142, 1);
          }
        }
      }
      .footer {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
        span {
          color: white;
        }
        img {
          height: 1rem;
        }
        margin-top: 1rem;
      }
    }
    @media screen and (max-width: 1000px) {
      flex-direction: column-reverse;
    }
  }
  .row {
    margin-bottom: 2.2rem;
  }
  .toggle-row {
    margin-top: 1.2rem;
    margin-bottom: 1.2rem;
  }
</style>
