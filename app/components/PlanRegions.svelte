<script>
	import { getContext } from "svelte";
	import Region from "./Region.svelte";

	export let region;

	const WebApp = getContext("webapp");

	const selectRegion = (event) => {
		console.log(`${event.target} selected`);
	};

	// TG desktop fix
	let viewportWidth = window.innerWidth;
	if (WebApp.platform == "tdesktop") {
		viewportWidth *= 0.97;
	}
</script>

<div class="headline">Select Plan</div>
<div class="regions" style="--vw:{viewportWidth}px">
	<Region
		double={true}
		--bg-color="linear-gradient(180deg, #5164A6 0%, #0E2267 91.67%)"
		on:click={selectRegion}>All Europe</Region>
	<Region --bg-color="#BF4747">Asia & Australia</Region>
	<Region --bg-color="#91CB7D">Latin America</Region>
	<Region --bg-color="#3B92AE">Middle East</Region>
	<Region singleCountry={true}>One Region</Region>
</div>

<style>
	.regions {
		display: flex;
		align-items: flex-start;
		align-content: flex-start;
		flex-wrap: wrap;
		gap: 9px;
	}
</style>
