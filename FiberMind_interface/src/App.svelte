<script>
	let message = '';
	let conversation = [];
	
	async function sendMessage() {
		const response = await fetch('/chat', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ message })
		});
		const data = await response.json();
		conversation = [...conversation, { role: 'user', content: message }, { role: 'assistant', content: data }];
		message = '';
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