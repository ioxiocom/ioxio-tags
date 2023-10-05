import { Apity } from "@cocreators-ee/apity"
import type { paths } from "./openapi"
import { settings } from "./settings"

const apity = Apity.for<paths>()

apity.configure({
  baseUrl: settings.PUBLIC_API_BASE_URL,
})

export const dataProduct = {
  fetch: apity
    .path("/dataproduct/fetch/{dataspace_domain}/{product_path}")
    .method("post")
    .create({ source: true }),
}
