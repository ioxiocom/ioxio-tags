import type { Option } from "$components/FormSelectGroup/index.svelte"

// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true

export const load = () => {
  const options: Option[] = []
  for (let i = 0; i < 20; i++) {
    options.push({
      id: `${i + 2}`,
      label: "Item #" + (i + 1),
    })
  }

  const productOptions: Option[] = [
    {
      id: "arbitrary",
      label: "Arbitrary",
    },
    {
      id: "premade",
      label: "Premade",
    },
  ]

  const signOptions: Option[] = [
    {
      id: "signed",
      label: "Signed",
    },
    {
      id: "unsigned",
      label: "Unsigned",
    },
  ]

  return {
    options,
    productOptions,
    signOptions,
  }
}
