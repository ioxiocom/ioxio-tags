import { env } from "$env/dynamic/public"

export const settings = {
  PUBLIC_API_BASE_URL: env.PUBLIC_API_BASE_URL || "http://localhost:8081",
  DOCUMENTATION_URL: "/documentation",
  ISS_DOMAIN: "tags.ioxio.dev",
}
