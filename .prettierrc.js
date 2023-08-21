module.exports = {
  printWidth: 100,
  trailingComma: "es5",
  useTabs: false,
  tabWidth: 2,
  semi: false,
  singleQuote: false,
  endOfLine: "lf",
  proseWrap: "always",
  plugins: ["prettier-plugin-svelte"],
  pluginSearchDirs: ["generator", "scanner"],
  overrides: [
    {
      files: "*.yaml",
      options: {
        proseWrap: "preserve",
      },
    },
    {
      files: "*.svelte",
      options: {
        parser: "svelte",
        proseWrap: "preserve",
      },
    },
  ],
}
