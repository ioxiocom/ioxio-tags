<script lang="ts">
  import Tooltip from "sv-tooltip"
  import FormInputGroup from "$components/FormInputGroup/index.svelte"
  import FormSelectGroup from "$components/FormSelectGroup/index.svelte"
  import FormCheckbox from "$components/FormCheckbox/index.svelte"
  import Button from "$components/Button/index.svelte"
  import Toggle from "$components/Toggle/index.svelte"
  import LogoTagsSvg from "$assets/ioxio-tags-logo.svg?url"
  import EffectSvg from "$assets/effect.svg?url"
  import LogomarkSvg from "$assets/ioxio-logomark.svg?url"
  import LogoSvg from "$assets/ioxio-logo.svg?url"
  import QuestionSvg from "$assets/question.svg?component"
  import SubtractSvg from "$assets/subtract.svg?url"
  import type { PageData } from "./$types"
  import { Status } from "./types"

  export let data: PageData

  let productOption: string
  let signOption: string
  let status: string = Status.READY
</script>

<svelte:head>
  <title>IOXIO Tags™️ generator</title>
  <meta name="description" content="IOXIO Tags™️ QR code generator demo application" />
</svelte:head>

<div class="container">
  <!-- Left Panel -->
  <div class="form-wrapper">
    <div class="title">Generate a product passport</div>
    <img class="logomarkSvg" src={LogomarkSvg} alt="" aria-hidden="true" />
    <form>
      <div class="row">
        <FormInputGroup
          name="domain"
          label="Issuer domain"
          placeholder="ex.tags.ioxio.dev"
          disabled={status === Status.GENERATING}
        />
      </div>
      <div class="row">
        <div class="toggle-row">
          <Toggle
            options={["Arbitrary", "Premade"]}
            bind:value={productOption}
            disabled={status === Status.GENERATING}
          />
        </div>
        <FormSelectGroup
          name="product"
          label="Product"
          placeholder="Type a product"
          options={data.options}
          disabled={status === Status.GENERATING}
        />
      </div>
      <div class="row">
        <FormInputGroup
          name="productId"
          label="Product ID"
          placeholder="ex. VV123456-12"
          disabled={status === Status.GENERATING}
        />
        <div class="toggle-row">
          <Toggle
            options={["Signed", "Unsigned"]}
            bind:value={signOption}
            disabled={status === Status.GENERATING}
          />
        </div>
      </div>
      <div class="row">
        <div class="col">
          <FormCheckbox
            name="valid"
            label="Create valid signature"
            disabled={status === Status.GENERATING}
          />
          <Tooltip tip="Whats this?" top>
            <span class="question-icon">
              <QuestionSvg />
            </span>
          </Tooltip>
        </div>
      </div>
      <div class="actions-wrapper">
        <Button
          disabled={status === Status.GENERATING}
          title="Generate IOXIO Tag"
          onClick={() => {
            status = Status.GENERATING
          }}
        />
      </div>
    </form>
  </div>
  <!-- Right Panel -->
  <div class="qrcode-area-wrapper">
    <div class="qrcode-area">
      <div class="qrcode">
        {#if status !== Status.GENERATING}
          <img class="frame" src={SubtractSvg} alt="" aria-hidden="true" />
        {:else}
          <div class="frame anim" />
        {/if}
        <img class="effect" src={EffectSvg} alt="" aria-hidden="true" />
        <img class="logo" src={LogoTagsSvg} alt="" aria-hidden="true" />
      </div>
    </div>
    <div class="status">
      {#if status === Status.READY}
        IOXIO Tag generator
      {:else if status === Status.GENERATING}
        Generating...
      {:else}
        Finished!
      {/if}
    </div>
    <div class="product-area">
      {#if status === Status.READY}
        <div class="description">
          <p>
            This application serves as a demonstration platform for generating QR codes specifically
            designed for Digital Product Passports.
          </p>
          <p>
            Utilizing the IOXIO Dataspace technology, this app showcases how QR codes can be
            generated to serve as digital passports for various Data Products. These QR codes can be
            read using a compatible reader application, enabling access to relevant product details
            in real time.
          </p>
          <a class="documentation" href="/">See documentation →</a>
        </div>
      {/if}
    </div>
    <div class="footer">
      <span>Made by</span>
      <img src={LogoSvg} alt="" aria-hidden="true" />
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
        flex: 0.7;
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
            text-decoration: none;
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
    display: flex;
    align-items: center;
    flex-direction: row;
    cursor: pointer;
  }
  .anim {
    overflow: hidden;
    border-radius: 20px;
    position: relative;
  }
  .anim::before {
    content: "";
    position: absolute;
    width: 100px;
    height: 200%;
    right: calc(50% - 50px);
    bottom: 50%;
    animation: rotate 4s linear infinite;
    transform-origin: bottom center;
  }
  .anim::after {
    content: "";
    position: absolute;
    background: #111920;
    inset: 2px;
    border-radius: 18px;
  }
  @keyframes rotate {
    0% {
      transform: rotate(0deg);
      background: linear-gradient(to right, #8ebfd3, #85f8c3);
    }
    25% {
      transform: rotate(120deg);
      background: linear-gradient(to right, #85f8c3, #8fbbd4);
    }
    50% {
      transform: rotate(240deg);
      background: linear-gradient(to right, #8fbbd4, #9a78e8);
    }
    100% {
      transform: rotate(360deg);
      background: linear-gradient(to right, #9a78e8, #8ebfd3);
    }
  }
</style>
