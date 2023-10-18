<script>
	import { getContext } from "svelte";
	import Region from "app/components/Region.svelte";

	const webapp = getContext("webapp");
	// TG desktop fix
	let viewportWidth = window.innerWidth;
	if (webapp.platform == "tdesktop") {
		viewportWidth *= 0.97;
	}
</script>

<div class="headline">Select Plan</div>
<div class="regions" style="--vw:{viewportWidth}px">
	<Region
		double={true}
		--bg-color="linear-gradient(180deg, #5164A6 0%, #0E2267 91.67%)"
		>All Europe</Region>
	<Region --bg-color="#BF4747">Asia & Australia</Region>
	<Region --bg-color="#91CB7D">Latin America</Region>
	<Region --bg-color="#3B92AE">Middle East</Region>
	<Region selector={true}>One Region</Region>
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
