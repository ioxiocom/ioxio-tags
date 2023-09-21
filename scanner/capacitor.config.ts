import { CapacitorConfig } from "@capacitor/cli"

const config: CapacitorConfig = {
  appId: "com.ioxio_tags_scanner.app",
  appName: "ioxio-tags-scanner",
  webDir: "build",
  server: {
    url: "http://192.168.1.131:5173",
    cleartext: true
  },
}

export default config
