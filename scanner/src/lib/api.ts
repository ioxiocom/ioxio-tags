import { Apity } from "@cocreators-ee/apity"
import type { paths } from "./openapi"
import { settings } from "./settings"

const apity = Apity.for<paths>()

apity.configure({
  baseUrl: settings.PUBLIC_API_BASE_URL,
})

export const fetchMetaDataV1 = apity.path("/tag/metadata/v1/").method("post").create()
