import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.ioxio_scanner.app',
  appName: 'ioxio-scanner',
  webDir: 'build',
  server: {
    androidScheme: 'https'
  }
};

export default config;
