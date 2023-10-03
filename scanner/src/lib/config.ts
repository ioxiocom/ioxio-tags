import { env } from "$env/dynamic/private"

export const config = {
  DEVELOPMENT: env.DEVELOPMENT === "true",
  PUBLIC_API_BASE_URL: env.PUBLIC_API_BASE_URL || "https://localhost:8081",
}
