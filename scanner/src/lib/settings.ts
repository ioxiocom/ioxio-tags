import { env } from "$env/dynamic/private"

export const settings = {
  DEVELOPMENT: env.DEVELOPMENT === "true",
  PUBLIC_API_BASE_URL: env.PUBLIC_API_BASE_URL || "http://localhost:8081",
}
