<script lang="ts">
  import Tooltip from "sv-tooltip"
  import FormInputGroup from "$components/FormInputGroup/index.svelte"
  import FormSelectGroup from "$components/FormSelectGroup/index.svelte"
  import FormCheckbox from "$components/FormCheckbox/index.svelte"
  import Button from "$components/Button/index.svelte"
  import Toggle from "$components/Toggle/index.svelte"
  import logoTagsSvg from "$assets/ioxio-tags-logo.svg?url"
  import effectSvg from "$assets/effect.svg?url"
  import logomarkSvg from "$assets/ioxio-logomark.svg?url"
  import logoSvg from "$assets/ioxio-logo.svg?url"
  import QuestionSvg from "$assets/question.svg?component"
  import subtractSvg from "$assets/subtract.png"
  import type { PageData } from "./$types"

  export let data: PageData

  let productOption: string
  let signOption: string
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
          <Toggle options={["arbitrary", "premade"]} bind:value={productOption} />
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
          <Toggle options={["signed", "unsigned"]} bind:value={signOption} />
        </div>
      </div>
      <div class="row">
        <div class="col">
          <FormCheckbox name="valid" label="Create valid signature" />
          <Tooltip tip="Whats this?" top>
            <span class="question-icon">
              <QuestionSvg />
            </span>
          </Tooltip>
        </div>
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
        <p>
          This application serves as a demonstration platform for generating QR codes specifically
          designed for Data Product Passports.
        </p>
        <p>
          Utilizing the IOXIO Dataspace technology, this app showcases how QR codes can be generated
          to serve as digital passports for various Data Products. These QR codes can be read using
          a compatible reader application, enabling access to relevant product details in real time.
        </p>
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
    display: flex;
    flex-direction: row;
    margin: auto;
    width: 100%;
    min-height: 100vh;
    overflow: hidden;
    .form-wrapper {
      padding: 7.5rem;
      background-color: white;
      width: 50%;
      position: relative;
      @media screen and (max-width: 1440px) {
        flex: 1;
        padding: 3rem;
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
        bottom: 2rem;
        left: -2%;
        z-index: 0;
      }
    }
    .qrcode-area-wrapper {
      padding: 1rem 3rem 1rem;
      background-color: #111920;
      width: 50%;
      display: flex;
      flex-direction: column;
      @media screen and (max-width: 1440px) {
        flex: 1;
        padding: 1rem 3rem;
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
        min-height: 26rem;
        .frame {
          width: 20rem;
          height: 20rem;
          position: absolute;
          left: -2rem;
          top: -2rem;
        }
        .qrcode {
          width: 16rem;
          height: 16rem;
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
        font-size: 2.125rem;
        font-weight: 400;
        text-align: center;
        padding: 1rem 0;
      }
      .product-area {
        flex: 1;
        margin-bottom: 5rem;
        .description {
          color: white;
          font-size: 1.2rem;
          p {
            text-align: justify;
          }
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
  .col {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .toggle-row {
    margin-top: 1.2rem;
    margin-bottom: 1.2rem;
  }
  .question-icon {
    margin-left: 1rem;
    display: flex !important;
    align-items: center !important;
    flex-direction: row !important;
    cursor: pointer;
  }
</style>
