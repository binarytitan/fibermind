<script>
	let message = '';
	let conversation = [];
	
	async function sendMessage() {
		if (message.trim() === '') {
			return;
		}
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
		scrollToBottom();
	}

	function handleKeydown(event) {
		if (event.key === 'Enter' && !event.shiftKey) {
			event.preventDefault();
			sendMessage();
		}
	}

	function scrollToBottom() {
		tick().then(() => {
			const chatDisplay = document.getElementById('chat-display');
			const lastMessage = chatDisplay.lastElementChild;
			if (lastMessage) {
				lastMessage.scrollIntoView();
			}
		});
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
		<input bind:value={message} on:keydown={handleKeydown} type="text" placeholder="Type your message here..." />
		<button on:click={sendMessage}>Send</button>
	</div>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 600px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 2em;
		font-weight: 100;
	}

	#chat-display {
		height: 400px;
		border: 1px solid #ccc;
		padding: 10px;
		margin-bottom: 10px;
		overflow-y: auto;
		background-color: #f8f8f8;
		border-radius: 10px;
	}

	#chat-input {
		display: flex;
	}

	#chat-input input {
		flex-grow: 1;
		margin-right: 10px;
		padding: 10px;
		border-radius: 10px;
		border: 1px solid #ccc;
	}

	#chat-input button {
		padding: 10px;
		background-color: #ff3e00;
		color: white;
		border: none;
		border-radius: 10px;
		cursor: pointer;
	}

	#chat-input button:hover {
		background-color: #ff5e3a;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>