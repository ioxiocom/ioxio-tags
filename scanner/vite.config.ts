import { NodeGlobalsPolyfillPlugin } from "@esbuild-plugins/node-globals-polyfill"

import { sveltekit } from "@sveltejs/kit/vite"
import { defineConfig } from "vite"

export default defineConfig({
  plugins: [sveltekit()],
  /*
  // Uncomment to debug the resulting code better - unless you really like reading obfuscated JS
  build: {
    minify: false
  },
  */
  optimizeDeps: {
    esbuildOptions: {
      // Node.js global to browser globalThis
      define: {
        global: "globalThis",
      },
      // Enable esbuild polyfill plugins
      plugins: [
        NodeGlobalsPolyfillPlugin({
          buffer: true,
        }),
      ],
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@import '$styles/variables.scss';`,
      },
    },
  },
})
