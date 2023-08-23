<script lang="ts">
    import { onMount } from 'svelte';
    import { BarcodeScanner, BarcodeScanResult } from '@capacitor-community/barcode-scanner';
  
    let scannedCode: string = "";
  
    async function scanBarcode() {
      const result: BarcodeScanResult = await BarcodeScanner.startScan();
      if (!result.cancelled) {
        scannedCode = result.text ?? "";
      }
    }
  
    onMount(() => {
      BarcodeScanner.prepare();
    });
  </script>
  
  <main>
    <h1>IOXIO Barcode Scanner</h1>
    <button on:click={scanBarcode}>Scan Barcode</button>
    {#if scannedCode}
      <p>Scanned Code: {scannedCode}</p>
    {/if}
  </main>
  
  <style>
    main {
      text-align: center;
      padding: 20px;
    }
  
    button {
      padding: 10px 20px;
      font-size: 16px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>  