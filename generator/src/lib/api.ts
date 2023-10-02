import { Apity } from "@cocreators-ee/apity"
import type { paths } from "$lib/openapi"
import { env } from "$env/dynamic/public"

const API_BASE_URL = env.PUBLIC_API_BASE_URL

const apity = Apity.for<paths>()
apity.configure({
  // Base URL to your API
  baseUrl: API_BASE_URL,
  // RequestInit options, e.g. default headers
  init: {
    headers: {
      Accept: "image/png",
      "Content-Type": "application/json",
    },
  },
})

export const generateSecureQrcode = apity.path("/tag/generate/secure/v1/").method("post").create()
