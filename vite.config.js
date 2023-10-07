import { defineConfig } from 'vite';
import { resolve } from 'path';
import { svelte } from '@sveltejs/vite-plugin-svelte';

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [svelte()],
	build: {
		rollupOptions: {
			input: {
				index: resolve(__dirname, 'index.html'),
				app: resolve(__dirname, 'app/index.html'),
			},
		},
	},
});