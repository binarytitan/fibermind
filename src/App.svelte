<script>
  import { onMount } from 'svelte';
  let message = '';
  let messages = [];

  onMount(async () => {
    const res = await fetch('/message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ messages: messages })
    });
    const data = await res.json();
    messages.push({ role: 'system', content: data.message });
  });

  async function sendMessage() {
    messages.push({ role: 'user', content: message });
    const res = await fetch('/message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ messages: messages })
    });
    const data = await res.json();
    messages.push({ role: 'assistant', content: data.message });
    message = '';
  }
</script>

<main>
  <div>
    {#each messages as msg (msg)}
      <p>{msg.role}: {msg.content}</p>
    {/each}
  </div>
  <input bind:value={message} on:keydown|preventDefault="Enter"={sendMessage}>
  <button on:click={sendMessage}>Send</button>
</main>
