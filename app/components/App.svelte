<script>
	import WebApp from "@twa-dev/sdk";

	import { onMount, setContext } from "svelte";

	import Logo from "./Logo.svelte";
	import Info from "./Info.svelte";
	import Plans from "./Plans.svelte";
	import Sim from "./SIM.svelte";
	import History from "./History.svelte";

	setContext("webapp", WebApp);

	let user = fetch(`/api/user?${WebApp.initData}`).then((response) =>
		response.json()
	);
</script>

<div class="container">
	{#await user}
		Loading
	{:then user}
		{#if !user.is_active}
			<Logo />
			<Info />
			<Plans />
			<History />
		{:else}
			Active
			<Sim />
			<!-- Buy More: -->
			<Plans />
			<History />
			<Info />
		{/if}
	{/await}
</div>

<style>
	.container {
		padding: 0 1em 0 1em;
	}
</style>
