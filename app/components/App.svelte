<script>
	import WebApp from "@twa-dev/sdk";

	import { onMount, setContext } from "svelte";

	import Logo from "./Logo.svelte";
	import Info from "./Info.svelte";
	import Plans from "./Plans.svelte";
	import Sim from "./SIM.svelte";
	import History from "./History.svelte";

	setContext("webapp", WebApp);

	let user = {};
	onMount(async () => {
		user = await fetch(`/api/user?${initData}`).then((data) => data.json());
	});

	console.log(WebApp.initData);
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
