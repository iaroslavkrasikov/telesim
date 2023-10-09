<script>
	import Counter from "./lib/Counter.svelte";

	import WebApp from "@twa-dev/sdk";

	const params = WebApp.initData;
	WebApp.MainButton.show();
	$: isv = WebApp.BackButton.isVisible;
	WebApp.MainButton.onClick(() => {
		WebApp.BackButton.isVisible = isv ? false : true;
	});
</script>

<main>
	<h3>This is Telesim TWA page.</h3>
	<p>WebApp params: <code></code></p>
	<Counter />
</main>

<style>
</style>
