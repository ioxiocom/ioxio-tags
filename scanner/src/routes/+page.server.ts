import { config } from "$lib/config"

export function load() {
  return {
    isDevelopment: config.DEVELOPMENT,
  }
}
