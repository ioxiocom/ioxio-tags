import { env } from "$env/dynamic/public"

export const settings = {
  DEVELOPMENT: env.PUBLIC_DEVELOPMENT === "true",
  PUBLIC_API_BASE_URL: env.PUBLIC_API_BASE_URL || "http://localhost:8081",
}
