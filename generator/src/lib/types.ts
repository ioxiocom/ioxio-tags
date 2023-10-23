export const ProductType = {
  ARBITRARY: "Arbitrary",
  PREMADE: "Premade",
} as const

export type ProductType = typeof ProductType[keyof typeof ProductType]

export const productTypes: ProductType[] = [ProductType.ARBITRARY, ProductType.PREMADE]

export const SignOption = {
  SIGNED: "Signed",
  UNSIGNED: "Unsigned",
} as const

export type SignOption = typeof SignOption[keyof typeof SignOption]

export const signOptions: SignOption[] = [SignOption.SIGNED, SignOption.UNSIGNED]
