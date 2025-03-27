<script lang="ts">
  import FormInputGroup from "$components/FormInputGroup/index.svelte"
  import FormSelectGroup from "$components/FormSelectGroup/index.svelte"
  import FormCheckbox from "$components/FormCheckbox/index.svelte"
  import Button from "$components/Button/index.svelte"
  import Toggle from "$components/Toggle/index.svelte"
  import IoxioTagsLogo from "$assets/ioxio-tags-logo.svg?url"
  import EffectSvg from "$assets/effect.svg?url"
  import LogomarkSvg from "$assets/ioxio-logomark.svg?url"
  import LogoSvg from "$assets/ioxio-logo.svg?url"
  import QuestionSvg from "$assets/question.svg?component"
  import SubtractSvg from "$assets/subtract.svg?url"
  import DownloadSvg from "$assets/download.svg?url"
  import WarnSvg from "$assets/warn.svg?url"
  import { Status } from "./types"
  import type { components } from "$lib/openapi"
  import { tag } from "$lib/api"
  import { settings } from "$lib/settings"
  import { ProductType, SignOption, productTypes, signOptions } from "$lib/types"
  import { premadeProducts } from "$lib/premadeProducts"
  import validator from "validator"

  let issValue: string = settings.ISS_DOMAIN
  let productType: string = ProductType.PREMADE
  let product: string
  let productId: string
  let signOption: string = SignOption.SIGNED
  let isValid: boolean = true

  let status: string = Status.READY
  let qrcodeElement: HTMLImageElement
  let error: string | null = null
  let issError: string | null = null

  function slugify(input: string): string {
    let value = input.toLowerCase().trim()
    value = value.replace(/[^.\w\s-]/, "")
    return value.replace("-s", "-")
  }

  async function onGenerate(event: SubmitEvent) {
    event.preventDefault()
    clearError()

    if (!product) {
      return
    }

    if (
      !validator.isFQDN(issValue, {
        require_tld: true,
        allow_underscores: true,
      })
    ) {
      issError = "Invalid domain"
      return
    }

    status = Status.GENERATING
    const iss = issValue
    const id = productId
    const valid = isValid

    // implementation by apity
    let generateRequest
    if (signOption === SignOption.SIGNED) {
      generateRequest = tag.generateSecureV1({ iss, product, id, valid })
    } else {
      generateRequest = tag.generateUrlV1({ iss, product, id })
    }
    const result = await generateRequest.result
    status = Status.FINISHED

    if (result?.ok) {
      var reader = new window.FileReader()
      reader.readAsDataURL(result.data as Blob)
      reader.onload = function () {
        var imageDataUrl = reader.result
        if (imageDataUrl) {
          qrcodeElement.setAttribute("src", imageDataUrl?.toString())
        }
      }
      return
    } else {
      if (result.status === 400) {
        error = result.data.error
      } else if (result.status === 422) {
        error = result.data.detail[0].msg
      } else {
        error = "Generating tag failed. Check developer console for details, or try again later."
        console.error("Generating tag failed", result)
      }
      status = Status.READY
    }
  }

  async function onDownloadQRcode() {
    // "Signed" and "Create valid signature" == "signed"
    // "Signed" and not "Create valid signature" == "invalid"
    // "Unsigned" == "unsigned"
    const security: "signed" | "invalid" | "unsigned" =
      signOption === SignOption.SIGNED ? (isValid ? "signed" : "invalid") : "unsigned"
    const filenameParts = [
      slugify(issValue),
      slugify(product),
      slugify(productId),
      `${security}.png`,
    ]

    const link = document.createElement("a")
    link.href = qrcodeElement.src
    link.download = filenameParts.join("_")
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  function clearError() {
    error = null
    issError = null
  }

  function onChangeIssValue(event: Event) {
    clearError()
    const target = event.target as HTMLInputElement
    issValue = target.value
  }

  function onChangeValidSignature(event: Event) {
    clearError()
    const target = event.target as HTMLInputElement
    isValid = target.checked
    if (isValid) {
      issValue = settings.ISS_DOMAIN
    }
  }

  function onChangeProductType(value: string) {
    clearError()
    productType = value
    productId = ""
    product = ""
  }

  function onChangeArbitraryProduct(event: Event) {
    clearError()
    const target = event.target as HTMLInputElement
    product = target.value
  }

  function onChangeProductId(event: Event) {
    clearError()
    const target = event.target as HTMLInputElement
    productId = target.value
  }

  function onChangePremadeProduct(event: CustomEvent) {
    clearError()
    productId = event.detail.id
    product = event.detail.product
  }

  function onChangeSignOption(value: string) {
    clearError()
    signOption = value
    if (signOption === SignOption.UNSIGNED) {
      isValid = false
    }
  }
</script>

<svelte:head>
  <title>IOXIO Tags™️ generator</title>
  <meta name="description" content="IOXIO Tags™️ QR code generator demo application" />
</svelte:head>

<div class="container">
  <!-- Left Panel -->
  <div class="form-wrapper">
    <div>
      <div class="title">Generate a product passport</div>
      <img class="logomarkSvg" src={LogomarkSvg} alt="" aria-hidden="true" />
      <form on:submit={onGenerate}>
        <div class="row">
          <FormInputGroup
            name="iss"
            label="Issuer domain"
            placeholder="ex.tags.ioxio.dev"
            bind:value={issValue}
            onChange={onChangeIssValue}
            disabled={status === Status.GENERATING || isValid}
            required
          />
          {#if issError}
            <p class="error">{issError}</p>
          {/if}
        </div>
        <div class="row">
          <div class="toggle-row">
            <Toggle
              options={productTypes}
              onChange={onChangeProductType}
              bind:value={productType}
              disabled={status === Status.GENERATING}
            />
          </div>
          {#if productType === ProductType.ARBITRARY}
            <FormInputGroup
              name="product"
              label="Product"
              placeholder=""
              required
              bind:value={product}
              onChange={onChangeArbitraryProduct}
            />
          {:else}
            <FormSelectGroup
              name="product"
              label="Product"
              placeholder="Type a product"
              options={premadeProducts}
              onSelect={onChangePremadeProduct}
              disabled={status === Status.GENERATING}
              required
            />
          {/if}
        </div>
        <div class="row">
          <FormInputGroup
            name="id"
            label="Product ID"
            placeholder="ex. VV123456-12"
            onChange={onChangeProductId}
            bind:value={productId}
            required
          />
          <div class="toggle-row">
            <Toggle
              options={signOptions}
              onChange={onChangeSignOption}
              bind:value={signOption}
              disabled={status === Status.GENERATING}
            />
          </div>
        </div>
        {#if signOption === SignOption.SIGNED}
          <div class="row">
            <div class="col">
              <FormCheckbox
                name="valid"
                bind:checked={isValid}
                label="Create valid signature"
                disabled={status === Status.GENERATING}
                onChange={onChangeValidSignature}
              />
              <span class="question-icon">
                <QuestionSvg />
                <div class="tooltip">
                  Leave this off if you want to test handling of corrupted/invalid signatures
                </div>
              </span>
            </div>
          </div>
        {/if}
        <div class="actions-wrapper">
          <Button
            disabled={status === Status.GENERATING}
            title="Generate IOXIO Tag"
            type="submit"
          />
        </div>
      </form>
    </div>
    {#if error}
      <div class="error-wrapper">
        <img src={WarnSvg} alt="" aria-hidden="true" />
        <p>{error}</p>
      </div>
    {/if}
  </div>
  <!-- Right Panel -->
  <div class="qrcode-area-wrapper">
    <div class="qrcode-area">
      <div class="qrcode-frame">
        {#if status !== Status.GENERATING}
          <img class="frame" src={SubtractSvg} alt="" aria-hidden="true" />
          <img class="logo" src={IoxioTagsLogo} alt="" aria-hidden="true" />
          {#if status === Status.FINISHED}
            <img class="qrcode" alt="" aria-hidden="true" src="" bind:this={qrcodeElement} />
          {/if}
        {:else}
          <div class="frame anim" />
        {/if}
        <img class="effect" src={EffectSvg} alt="" aria-hidden="true" />
      </div>
    </div>
    <div class="status">
      {#if status === Status.READY}
        IOXIO Tags™ generator
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
          <a class="documentation" href={settings.TAGS_DOCS_URL} target="_blank" rel="noreferrer">
            See documentation →
          </a>
        </div>
      {:else if status === Status.FINISHED}
        <div class="result">
          <p class="label">Issuer domain</p>
          <p class="value">{issValue}</p>
          <p class="label">Product</p>
          <p class="value">{product}</p>
          <p class="label">Product ID</p>
          <p class="value">{productId}</p>
          <div class="download">
            <Button title="Download QR code" icon={DownloadSvg} onClick={onDownloadQRcode} />
          </div>
        </div>
      {:else}
        <div />
      {/if}
    </div>
    <a href="https://ioxio.com/" class="footer" target="_blank" rel="noreferrer">
      <span>Made by</span>
      <img src={LogoSvg} alt="" aria-hidden="true" />
    </a>
  </div>
</div>

<style lang="scss">
  .container {
    display: flex;
    flex-direction: row;
    margin: auto;
    width: 100%;
    @media screen and (min-width: 90rem) {
      max-width: 90rem;
      max-height: 64rem;
      min-width: 90rem;
    }
    @media screen and (max-width: 90rem) {
      min-height: 100vh;
    }
    .form-wrapper {
      padding: 7.5rem;
      background-color: white;
      width: 50%;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: center;
      border-top-left-radius: 0.9375rem;
      border-bottom-left-radius: 0.9375rem;
      @media screen and (max-width: 90rem) {
        flex: 1;
        padding: 3rem;
        border-top-left-radius: 0rem;
        border-bottom-left-radius: 0rem;
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
        .error {
          margin: 0.5rem 0;
          color: #dd596a;
          font-size: 0.8rem;
          font-weight: 400;
        }
      }
      .actions-wrapper {
        margin-top: 4rem;
      }
      .logomarkSvg {
        width: 80%;
        position: absolute;
        bottom: 2rem;
        left: -5%;
        z-index: 0;
        display: none;
        opacity: 0.2;
        @media screen and (max-width: 90rem) {
          display: block;
        }
      }
    }
    .error-wrapper {
      margin-top: 4rem;
      box-shadow: 0px 1px 2px 0px #1018280d;
      border: 1px solid #ccd5e1;
      border-radius: 0.3125rem;
      padding: 1rem;
      position: relative;
      background: #ffffff;
      color: #dd596a;
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 1rem;
      p {
        margin: 0;
        font-size: 0.75rem;
        font-weight: 400;
        line-height: 1.125rem;
      }
    }
    .qrcode-area-wrapper {
      padding: 1rem 3rem 1rem;
      background-color: #111920;
      width: 50%;
      display: flex;
      flex-direction: column;
      border-top-right-radius: 0.9375rem;
      border-bottom-right-radius: 0.9375rem;
      @media screen and (max-width: 90rem) {
        flex: 1;
        padding: 1rem 3rem;
        border-top-right-radius: 0rem;
        border-bottom-right-radius: 0rem;
      }
      @media screen and (max-width: 62.5rem) {
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
          position: absolute;
          left: 0rem;
          top: 0rem;
          z-index: 2;
        }
        .qrcode-frame {
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
        text-decoration: none;
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

  .result {
    .label {
      color: #828282;
      font-size: 1rem;
      font-weight: 400;
      margin-bottom: 0.3rem;
      margin-top: 0;
    }
    .value {
      color: #eeefec;
      font-size: 1rem;
      font-weight: 400;
      margin-bottom: 1rem;
      margin-top: 0;
    }
  }
  .download {
    display: flex;
    :global(button) {
      position: relative;
      width: 100%;
      background: linear-gradient(45deg, #9a75e9 0%, #85fbc2 100%) !important;
      &::after {
        content: "";
        position: absolute;
        width: calc(100% - 3px);
        height: calc(100% - 3px);
        top: 1.5px;
        left: 1.5px;
        border-radius: 0.3125rem;
        background-color: #111920;
      }
    }
  }
  .row {
    margin-bottom: 2.125rem;
  }
  .col {
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .toggle-row {
    margin-top: 1rem;
    margin-bottom: 1rem;
  }
  .question-icon {
    margin-left: 1rem;
    display: flex;
    align-items: center;
    flex-direction: row;
    position: relative;
    &:hover .tooltip {
      visibility: visible;
      opacity: 1;
    }
    .tooltip {
      position: absolute;
      left: calc(100% + 0.625rem);
      visibility: hidden;
      color: #101920;
      font-size: 0.75rem;
      font-style: normal;
      font-weight: 400;
      line-height: 1.125rem;
      padding: 0.5rem 0.75rem;
      border-radius: 0.3125rem;
      width: 15rem;
      box-shadow: 0px 0px 4px 0px rgba(0, 0, 0, 0.15);
      opacity: 0;
      transition: opacity 0.15s;

      &::before {
        content: "";
        position: absolute;
        left: -0.3125rem;
        top: calc(50% - 0.5rem);
        border-top: 0.5rem solid transparent;
        border-right: 0.3125rem solid #ffffff;
        border-bottom: 0.5rem solid transparent;
        filter: drop-shadow(0px 0px 4px rgba(0, 0, 0, 0.15));
        z-index: 0;
      }
    }
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

  @-webkit-keyframes fadeIn {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  @keyframes fadeIn {
    0% {
      opacity: 0;
    }
    100% {
      opacity: 1;
    }
  }

  .fadeIn {
    -webkit-animation-name: fadeIn;
    animation-name: fadeIn;
  }
</style>
