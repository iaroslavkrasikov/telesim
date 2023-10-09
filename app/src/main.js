import eruda from 'eruda';
import App from './App.svelte';

eruda.init();

const app = new App({
	target: document.getElementById('app')
});

export default app;