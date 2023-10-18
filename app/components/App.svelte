<script>
	import WebApp from "@twa-dev/sdk";

	import { onMount, setContext } from "svelte";

	import Logo from "app/components/Logo.svelte";
	import Info from "app/components/Info.svelte";
	import Plans from "app/components/Plans.svelte";
	import Sim from "app/components/SIM.svelte";
	import History from "app/components/History.svelte";

	setContext("webapp", WebApp);

	let user = {};
	onMount(async () => {
		user = await fetch(`/api/user?${initData}`).then((data) => data.json());
	});

	console.log(user);
</script>

<div class="container">
	<!-- {#if !user.isActive} -->
	{#if true}
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
