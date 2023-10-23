import { env } from "$env/dynamic/public"

export const settings = {
  PUBLIC_API_BASE_URL: env.PUBLIC_API_BASE_URL || "http://localhost:8081",
  DOCUMENTATION_URL: "https://docs.ioxio.dev/tags",
  IOXIO_URL: "https://ioxio.com/",
  ISS_DOMAIN: "tags.ioxio.dev",
}
