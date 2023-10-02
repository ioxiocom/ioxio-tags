import { Apity } from "@cocreators-ee/apity"
import type { paths } from "./openapi"

const apity = Apity.for<paths>()

apity.configure({
  // TODO: Read URL from settings. Change to http://localhost:8081 locally
  baseUrl: "https://api.tags.ioxio.dev",
})

export const dataProduct = {
  fetch: apity
    .path("/dataproduct/fetch/{dataspace_domain}/{product_path}")
    .method("post")
    .create({ source: true }),
}
