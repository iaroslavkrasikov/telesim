<script>
	export let link;
	export let icon;
	export let text;

	// TODO: Button action
</script>

<button class="button" {link}>
	<img src={icon} class="icon" alt="" />
	<div>{text}</div>
</button>

<style>
	.button {
		display: inline-flex;
		height: 36px;
		padding: 0px 24px 0px 12px;
		align-items: center;
		flex-shrink: 0;
		font-weight: 590;
		line-height: 100%;
		vertical-align: middle;
		background: var(--tg-theme-button-color);
		border-radius: 12px;
		gap: 6px;
	}
	.icon {
		width: 24px;
		height: 24px;
	}
</style>
