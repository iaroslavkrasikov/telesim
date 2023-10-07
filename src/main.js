import './app.css';
import App from './App.svelte';

import WebApp from '@twa-dev/sdk';

WebApp.ready();

const app = new App({
	target: document.getElementById('app')
});

export default app;