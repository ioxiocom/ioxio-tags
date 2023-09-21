import { SplashScreen } from '@capacitor/splash-screen';
import '@fontsource/poppins';

export const prerender = true

const showSplashScreen = async () => {
  // Hide the splash (you should do this on app launch)
  await SplashScreen.hide();

  // Show the splash for an indefinite amount of time:
  await SplashScreen.show({
    autoHide: false,
  });

  // Show the splash for two seconds and then automatically hide it:
  await SplashScreen.show({
    showDuration: 2000,
    autoHide: true,
  });
};

// showSplashScreen();