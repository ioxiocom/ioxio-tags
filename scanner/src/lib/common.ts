import { toast } from '@zerodevx/svelte-toast'

export function consoleLog(message: string, type: string = "info")  {
  toast.push(message, { classes: [type === "info" ? "info" : "warn"] })
  if (type === "info") {
    console.log(message);
  } else {
    console.error(message);
  }
}