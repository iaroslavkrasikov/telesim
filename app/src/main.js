import App from './App.svelte';

// TODO: Remove eruda
import eruda from 'eruda';
import.meta.env.MODE == 'development' ? eruda.init() : null;

const app = new App({
	target: document.getElementById('app'),
});

export default app;