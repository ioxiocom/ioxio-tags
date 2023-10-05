<script lang="ts">
  import { onMount } from "svelte"
  import { page } from "$app/stores"
  import Loading from "$components/Loading/index.svelte"
  import { dataProduct } from "$lib/api"
  import { redirect } from "@sveltejs/kit"
  import { goto } from "$app/navigation"

  onMount(async () => {
    // Just an example of fetching a data product
    const { dataspace_domain, product_path, source, product, id } = history.state

    if (!dataspace_domain || !product_path || !product || !id) {
      goto("/")
      return
    }

    const result = await dataProduct.fetch({
      dataspace_domain,
      product_path,
      source,
      product,
      id,
    }).result

    if (result.ok) {
      goto(
        `/q/${encodeURIComponent(dataspace_domain)}/${encodeURIComponent(
          product_path
        )}/${encodeURIComponent(id)}`,
        {
          replaceState: true,
          state: result.data,
        }
      )
    } else {
      console.error("Generating tag failed", result)
    }
  })
</script>

<div class="content">
  <Loading type="light" />
</div>

<style lang="scss">
  .content {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
