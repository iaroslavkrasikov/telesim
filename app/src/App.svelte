<script>
	import WebApp from "@twa-dev/sdk";

	import Logo from "./lib/Logo.svelte";
	import Plans from "./lib/Plans.svelte";
	import Sim from "./lib/SIM.svelte";
	import History from "./lib/History.svelte";
	import Info from "./lib/Info.svelte";

	const checkInitData = (unsafeInitData) => {
		true
	} 

	const isUserActive = (userId)

	let initData = checkInitData(WebApp.initData)
		? WebApp.initDataUnsafe
		: undefined;

	const user = {
		name: initData.user.id,
		isActive: isUserActive(initData.user.id)
	};
</script>

<main>
	{#if !user.isActive}
		<Logo />
		<Info />
		<Plans />
		<History />
	{:else}
		<Sim />
		Buy More:
		<Plans />
		<History />
		<Info />
	{/if}
</main>

<style>
</style>
