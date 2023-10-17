import './app.css';

import eruda from 'eruda';

import App from './App.svelte';

// Use eruda in development

import.meta.env.MODE == "development" ? eruda.init() : null;

const app = new App({
	target: document.getElementById('app'),
});

export default app;