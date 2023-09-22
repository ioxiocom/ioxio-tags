<script lang="ts">
  export let name: string
  export let label: string = ""
</script>

<div class="wrapper">
  <div class="checkbox">
    <input type="checkbox" id={name} />
    <label for={name} style="--size: 20px">
      <svg viewBox="-10,-10,70,70">
        <path d="M5 30 L 20 45 L 45 5" />
      </svg>
    </label>
  </div>
  <span>{label}</span>
</div>

<style>
  .wrapper {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 0.5rem;
    color: rgba(16, 25, 32, 1);
  }
  .checkbox *,
  .checkbox *:after,
  .checkbox *:before {
    box-sizing: border-box;
  }

  .checkbox input {
    position: absolute;
    opacity: 0;
  }

  .checkbox input:checked + label svg path {
    stroke-dashoffset: 0;
  }

  .checkbox input:focus + label {
    transform: scale(1.03);
  }

  .checkbox input + label {
    display: block;
    border: 1.5px solid #21a796;
    width: var(--size);
    height: var(--size);
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
  }

  .checkbox input + label:active {
    transform: scale(1.05);
    border-radius: 12px;
  }

  .checkbox input + label svg {
    pointer-events: none;
    padding: 5%;
  }

  .checkbox input + label svg path {
    fill: none;
    stroke: #21a796;
    stroke-width: 8px;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-dasharray: 100;
    stroke-dashoffset: 101;
    transition: all 250ms cubic-bezier(1, 0, 0.37, 0.91);
  }
</style>
