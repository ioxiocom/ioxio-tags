import { toast } from "@zerodevx/svelte-toast"

const locale = new Intl.NumberFormat().resolvedOptions().locale
const NumberFormat = new Intl.NumberFormat(locale, {minimumSignificantDigits: 1})

export function consoleLog(message: string, type: string = "info") {
  toast.push(message, { classes: [type === "info" ? "info" : "warn"] })
  if (type === "info") {
    console.log(message)
  } else {
    console.error(message)
  }
}

export function formatNumber(input: number, unit = ""): string {
  if (input === 0 || input === null || input === undefined) {
    return "-"
  }

  let result = NumberFormat.format(input)
  if (unit) {
    result += ` ${unit}`
  }
  return result
}
