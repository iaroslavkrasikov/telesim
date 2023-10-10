<script>
	import WebApp from "@twa-dev/sdk";

	import Logo from "./lib/Logo.svelte";
	import Plans from "./lib/Plans/Plans.svelte";
	import Sim from "./lib/SIM/SIM.svelte";
	import History from "./lib/History.svelte";
	import Info from "./lib/Info/Info.svelte";
	import { setContext } from "svelte";

	setContext("webapp", WebApp);

	const checkInitData = (unsafeInitData) => {
		return true;
	};

	const isUserActive = (userId) => {
		return false;
	};

	let initData = checkInitData(WebApp.initData)
		? WebApp.initDataUnsafe
		: null;

	const user = {
		name: initData.user.id,
		isActive: isUserActive(initData.user.id),
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
