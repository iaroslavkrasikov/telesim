<script>
	import WebApp from "@twa-dev/sdk";

	import Logo from "./Logo.svelte";
	import Info from "./Info.svelte";
	import Plans from "./Plans.svelte";
	import Sim from "./SIM.svelte";
	import History from "./History.svelte";
	import { setContext } from "svelte";

	setContext("webapp", WebApp);

	const user = () => {
		fetch("/bot/api/init", {
			method: "POST",
			headers: { "Content-Type": "text/plain" },
			body: WebApp.initData,
		});
	};
</script>

<div class="container">
	{#if !user.isActive}
		<Logo />
		<Info />
		<Plans />
		<History />
	{:else}
		<Sim />
		<!-- Buy More: -->
		<Plans />
		<History />
		<Info />
	{/if}
</div>

<style>
	.container {
		padding: 0 1em 0 1em;
	}
</style>
