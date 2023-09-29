<script lang="ts">
  import Effect from "$assets/effect.svg"
  import IoxioLogo from "$assets/ioxio-logo.svg"
  import IoxioTagLogo from "$assets/ioxio-tag-logo.svg"
  import Circle from "$assets/circle.svg"
</script>

<div class="container">
  <div class="background" />
  <div class="animation-wrapper">
    <img class="circle second" src={Circle} alt="" aria-hidden="true" />
    <img class="circle first" src={Circle} alt="" aria-hidden="true" />
    <img class="circle third" src={Circle} alt="" aria-hidden="true" />
    <img class="logo" src={IoxioTagLogo} alt="" aria-hidden="true" />
    <img class="effect" src={Effect} alt="" aria-hidden="true" />
  </div>
  <div class="logo">
    <p>Made by</p>
    <img src={IoxioLogo} alt="" aria-hidden="true" />
  </div>
</div>

<style lang="scss">
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
    background: transparent;
    position: relative;
  }
  .animation-wrapper {
    position: absolute;
    left: 50%;
    top: 20vh;
    transform: translateX(-50%);
    width: 30vh;
    height: 30vh;
    .logo {
      position: absolute;
      width: 80%;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
    }
    .effect {
      position: absolute;
      width: 150%;
      height: auto;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      animation: fade 2s linear infinite;
    }
  }
  .circle {
    width: 100%;
    height: 100%;
    position: absolute;
    left: 0;
    top: 0;
    transform: translate(-50%, -50%);
  }
  .first {
    animation: anim1 2s linear infinite;
    z-index: 1;
  }
  .second {
    animation: anim2 2s linear infinite;
    z-index: 2;
  }
  .third {
    animation: anim3 2s linear infinite;
    z-index: 3;
  }
  .logo {
    position: absolute;
    bottom: 3rem;
    display: flex;
    left: 50%;
    transform: translateX(-50%);
    flex-direction: column;
    align-items: center;
    color: white;
    p {
      margin-bottom: 0.3rem;
    }
    img {
      width: 6rem;
    }
  }

  @keyframes anim1 {
    0% {
      transform: rotate(360deg) translate(0.8rem);
    }
    100% {
      transform: rotate(0deg) translate(0.8rem);
    }
  }
  @keyframes anim2 {
    0% {
      transform: rotate(360deg) translate(0px);
    }
    100% {
      transform: rotate(0deg) translate(0px);
    }
  }
  @keyframes anim3 {
    0% {
      transform: rotate(360deg) translate(-0.8rem);
    }
    100% {
      transform: rotate(0deg) translate(-0.8rem);
    }
  }
  @keyframes fade {
    0% {
      opacity: 0.6;
    }
    50% {
      opacity: 1;
    }
    100% {
      opacity: 0.6;
    }
  }
</style>
