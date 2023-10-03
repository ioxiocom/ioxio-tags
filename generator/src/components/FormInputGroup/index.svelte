<script lang="ts">
  export let name: string
  export let label: string
  export let placeholder: string | undefined
  export let disabled: boolean = false
  export let required: boolean = false
</script>

<div class="form-group">
  <label for={name}>{label}</label>
  <input id={name} type="text" {disabled} {name} {placeholder} {required} />
</div>

<style lang="scss">
  .form-group {
    label {
      display: block;
      font-size: 1rem;
      margin-bottom: 0.5rem;
      color: rgba(16, 25, 32, 1);
    }
    input {
      height: 38px;
      width: 100%;
      border: 1px solid #ccc;
      border-radius: 0.3rem;
      padding-left: 0.5rem;
      padding-right: 0.5rem;
      box-shadow: 0px 1px 2px 0px rgba(16, 24, 40, 0.05);
      &:not(:disabled):focus-visible {
        outline: none;
        border: 1px solid #555;
      }
      &:not(:disabled):active {
        border: 1px solid #555;
      }
      &::placeholder {
        color: rgba(217, 217, 217, 1);
      }
    }
  }
</style>
