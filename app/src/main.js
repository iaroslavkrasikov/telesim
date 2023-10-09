import eruda from 'eruda';
import App from './App.svelte';

import.meta.env.MODE == 'development' ? eruda.init() : null;

const app = new App({
	target: document.getElementById('app')
});

export default app;