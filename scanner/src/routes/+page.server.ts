import { DEVELOPMENT } from '$env/static/private';

export function load() {
	return {
    isDevelopment: DEVELOPMENT === "true"
  }
}