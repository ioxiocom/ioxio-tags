import { settings } from "$lib/settings"

export function load() {
  return {
    isDevelopment: settings.DEVELOPMENT,
  }
}
