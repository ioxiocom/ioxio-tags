<div class={`subtitle ${$$props.class}`}>
  <slot />
</div>

<style lang="scss">
  .subtitle {
    font-size: 0.75rem;
    font-weight: 400;
    color: white;
    margin-bottom: 1rem;

    &.no-bottom-margin {
      margin-bottom: 0;
    }
  }
</style>
