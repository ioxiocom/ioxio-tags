# IOXIO Tags™️ generator

Frontend for generating IOXIO Tags™️

## Developing

Install dependencies and run the project in development mode:

```bash
pnpm run dev
```

## Building

To test building the project:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

Testing Docker image:

```shell
cd generator
docker build . -t generator
docker run --rm -p 8080:8080 -it generator
```
