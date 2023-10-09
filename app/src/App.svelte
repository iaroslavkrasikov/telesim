<script>
	import Counter from "./lib/Counter.svelte";

	import WebApp from "@twa-dev/sdk";

	const params = WebApp.initData;
</script>

<main>
	<h3>This is Telesim TWA page.</h3>
	<p>WebApp params: <code>{params}</code></p>
	<Counter />
</main>

<style>
</style>
