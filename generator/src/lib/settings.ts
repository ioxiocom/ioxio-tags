import { env } from "$env/dynamic/public"

export const settings = {
  PUBLIC_API_BASE_URL: env.PUBLIC_API_BASE_URL || "http://localhost:8081",
  TAGS_DOCS_URL: "https://docs.ioxio.dev/tags",
  ISS_DOMAIN: "tags.ioxio.dev",
}
