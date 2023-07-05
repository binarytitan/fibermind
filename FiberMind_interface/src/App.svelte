<script>
	let message = '';
	let conversation = [];
	
	function sendMessage() {
		// We'll fill this in later to send the message to the server
	}
</script>

<main>
	<h1>Chatbot</h1>
	<div id="chat-display">
		{#each conversation as item (item.id)}
			<p><strong>{item.role}:</strong> {item.content}</p>
		{/each}
	</div>
	<div id="chat-input">
		<input bind:value={message} type="text" placeholder="Type your message here..." />
		<button on:click={sendMessage}>Send</button>
	</div>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>