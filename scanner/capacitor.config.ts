import { CapacitorConfig } from "@capacitor/cli"

const config: CapacitorConfig = {
  appId: "com.ioxio_tags_scanner.app",
  appName: "ioxio-tags-scanner",
  webDir: "build",
  server: {
    androidScheme: "https",
  },
}

export default config
