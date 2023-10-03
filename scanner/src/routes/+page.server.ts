import { settings } from "$lib/config"

export function load() {
  return {
    isDevelopment: settings.PUBLIC_API_BASE_URL === "true",
  }
}
