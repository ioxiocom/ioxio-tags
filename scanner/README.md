# IOXIO Tags Scanner™️ demo application

## Developing

```bash
pnpm run dev
```

## Building

```bash
pnpm run build
```

Testing Docker image:

```shell
docker build . -t scanner
docker run --rm -p 8080:8080 -it scanner
```

## iOS

TODO: Document most of this

```bash
pnpm run build
pnpm run ios
```

## Android

You will need OpenJDK 17 installed and configured correctly for your system for the Android builds
to work.

The following is for \*nix use, Windows use is likely very similar:

```shell
pnpm run build
pnpm run android
cd android
./gradlew
```

You can then open the `android` folder in [Android Studio](https://developer.android.com/studio),
set up your emulator or whatever and click the Play -icon.
