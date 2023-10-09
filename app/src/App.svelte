<script>
	import Counter from "./lib/Counter.svelte";

	import WebApp from "@twa-dev/sdk";
	// WebApp.ready();

	const initData = WebApp.initData;
	const validateData = () => {};
	// const sent = WebApp.sendData(WebApp.platform);

</script>

<main>
	<h3>This is Telesim TWA page.</h3>
	<p>WebApp params: <code>{WebApp.platform}</code></p>
	<Counter />
</main>

<style>
</style>
