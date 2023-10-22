<script>
	import PlanRegions from "./PlanRegions.svelte";
	import PlanLimits from "./PlanLimits.svelte";

	let region;
</script>

<div class="plans">
	<PlanRegions bind:region />
	<PlanLimits />
</div>

<style>
	.plans {
		margin-top: 2em;
	}
</style>
