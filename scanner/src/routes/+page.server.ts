import { settings } from "$lib/config"

export function load() {
  return {
    isDevelopment: settings.DEVELOPMENT,
  }
}
