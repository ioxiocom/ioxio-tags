<script lang="ts">
  import Svelecte from "svelecte"

  export let name: string
  export let label: string
  export let placeholder: string = ""
  export let options = []
  export let disabled: boolean = false
  export let required: boolean = false
  export let value: string
</script>

<div class="form-group">
  <label for={name}>{label}</label>
  <Svelecte inputId={name} {required} {disabled} {options} {placeholder} bind:value />
</div>

<style lang="scss">
  .form-group {
    label {
      display: block;
      font-size: 1rem;
      margin-bottom: 0.5rem;
      color: rgba(16, 25, 32, 1);
    }
  }
  :global(.form-group > .svelecte .sv-control.is-disabled) {
    background-color: rgba(239, 239, 239, 0.3);
    border-color: #ccc;
  }
</style>
