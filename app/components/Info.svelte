<script>
	import faqIcon from "../assets/icon/faq.svg";
	import devicesIcon from "../assets/icon/devices.svg";
	import supportIcon from "../assets/icon/support.svg";

	import InfoButton from "./InfoButton.svelte";
</script>

<div class="info">
	<InfoButton link="faq" icon={faqIcon} text="FAQ" />
	<InfoButton link="devices" icon={devicesIcon} text="eSIM Devices" />
	<InfoButton link="support" icon={supportIcon} text="Support" />
</div>

<style>
	.info {
		display: flex;
		margin-top: 2em;
		flex-wrap: wrap;
		color: var(--tg-theme-button-text-color);
		gap: 9px;
	}
</style>
