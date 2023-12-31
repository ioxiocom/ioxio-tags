import { Apity } from "@cocreators-ee/apity"
import type { paths } from "$lib/openapi"
import { settings } from "./settings"

const apity = Apity.for<paths>()
apity.configure({
  baseUrl: settings.PUBLIC_API_BASE_URL,
})

export const tag = {
  generateSecureV1: apity.path("/tag/generate/secure/v1/").method("post").create(),
  generateUrlV1: apity.path("/tag/generate/url/v1/").method("post").create(),
}
