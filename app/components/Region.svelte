<script>
	export let double = false;
	export let singleCountry = false;
</script>

<div>
	{#if !singleCountry}
		{#if double}
			<div class="region region-double">
				<div class="body-semibold"><slot /></div>
			</div>
		{:else}
			<div class="region">
				<div class="body-semibold"><slot /></div>
			</div>
		{/if}
	{:else}
		<div class="region region-selector">
			<div class="body-semibold"><slot /></div>
		</div>
	{/if}
</div>

<style>
	.region {
		--W: calc(var(--vw) - 2em);
		--g: 9px;
		--w: calc((var(--W) - 2 * var(--g)) / 3);
		display: flex;
		width: var(--w);
		height: var(--w);
		padding: 8px 12px;
		flex-direction: column;
		justify-content: flex-end;
		align-items: flex-start;
		flex-shrink: 0;
		background: var(--bg-color);
		color: #fff;
		border-radius: 12px;
	}

	.region-double {
		--u: calc(var(--W) - var(--w) - var(--g));
		width: var(--u);
	}

	.region-selector {
		background: var(--tg-theme-hint-color);
	}
</style>
