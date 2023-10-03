import { env } from "$env/dynamic/private"

export const settings = {
  DEVELOPMENT: env.DEVELOPMENT,
  PUBLIC_API_BASE_URL: env.PUBLIC_API_BASE_URL || "https://localhost:8081",
}