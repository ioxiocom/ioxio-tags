export const ProductType = {
  ARBITRARY: "Arbitrary",
  PREMADE: "Premade",
} as const

export type ProductType = typeof ProductType[keyof typeof ProductType]

export const productTypes: ProductType[] = [ProductType.ARBITRARY, ProductType.PREMADE]
