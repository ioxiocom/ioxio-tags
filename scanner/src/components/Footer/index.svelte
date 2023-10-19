<script lang="ts">
  import IoxioLogoSvg from "$assets/ioxio-logo.svg"
  import { settings } from "$lib/settings"
</script>

<a href={settings.IOXIO_URL} class="wrapper">
  <p>Made by</p>
  <img class="logo" src={IoxioLogoSvg} alt="IOXIO" />
</a>

<style>
  .wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-top: 1rem;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5rem;
    gap: 0.2rem;
    color: white;
    text-decoration: none;
  }
  .logo {
    height: 1rem;
  }
</style>
