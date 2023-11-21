<script>
  import { settings } from "../lib/settings"
</script>

<main>
  <h1>IOXIO Tags™️</h1>
  <div>
    <p>
      This is our demonstration platform for generating QR codes specifically designed for Digital
      Product Passports.
    </p>
    <p>
      Utilizing the IOXIO Dataspace™️ technology, these demos showcase how QR codes can be generated
      to serve as digital product passports for various uses. These QR codes can be read using any
      compatible reader application, enabling access to relevant product details in real time.
    </p>
  </div>
  <section>
    <a href={settings.SCANNER_URL} target="_blank">
      <div class="card">Scan IOXIO Tags</div>
    </a>
    <a href={settings.GENERATOR_URL} target="_blank">
      <div class="card">Generate tags</div>
    </a>
    <a href={settings.IOXIO_URL} target="_blank">
      <div class="card">Documentation</div>
    </a>
  </section>
  <footer>
    Made by <a href="https://ioxio.com" target="_blank">IOXIO®️</a>
  </footer>
</main>

<style>
  main {
    display: flex;
    flex-direction: column;

    gap: 2rem;
    margin: 2rem;
  }

  h1 {
    margin: 0;
  }

  p {
    margin-top: 0;
  }

  section {
    display: flex;
    flex-direction: row;
    gap: 2rem;
    flex-grow: 1;
  }

  a {
    color: #fff;
    text-decoration: none;
  }

  div.card {
    padding: 2rem;
    border: 1px solid #333;
    border-radius: 5px;
    background: rgb(27, 47, 58);
  }

  footer {
    border-top: 1px solid rgb(27, 47, 58);
    padding: 1rem 0;
    text-align: center;
  }
</style>
