<script lang="ts">
  import TruckIcon from "$assets/truck.svg"
  import ShipIcon from "$assets/ship.svg"

  export let origin: string
  export let destination: string
  export let isTruck: boolean = true
  export let isTotal: boolean = false
</script>

<div class="wrapper">
  <div class="cities">
    <span>{origin}</span>
    <span>{destination}</span>
  </div>
  <div class="road">
    <div class="line" />
    <div class="circle left" style="--size: 1rem;" />
    {#if !isTotal}
      <div class="circle center" style="--size: 2.25rem;">
        <img src={isTruck ? TruckIcon : ShipIcon} alt="" aria-hidden="true" />
      </div>
    {/if}
    <div class="circle right" style="--size: 1rem;" />
  </div>
</div>

<style lang="scss">
  .wrapper {
    margin-bottom: 1rem;
    .cities {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.5rem;
    }
    .road {
      height: 2.25rem;
      display: flex;
      align-items: center;
      position: relative;
      .line {
        width: 100%;
        height: 0.1875rem;
        background-color: #3cb08e;
      }
      .circle {
        width: var(--size);
        height: var(--size);
        border-radius: 50%;
        background-color: #3cb08e;
        position: absolute;
        top: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .left {
        left: 0;
        transform: translateY(-50%);
      }
      .right {
        right: 0;
        transform: translateY(-50%);
      }
      .center {
        left: 50%;
        transform: translate(-50%, -50%);
      }
    }
  }
</style>
