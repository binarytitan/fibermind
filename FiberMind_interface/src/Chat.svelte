<script>
    import { onMount } from 'svelte';
    let messages = [];
    let input = '';

    async function sendMessage() {
        const response = await fetch('http://localhost:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: input })
        });
        const data = await response.json();

        messages = [...messages, { role: 'user', content: input }, { role: 'bot', content: data }];
        input = '';
    }
</script>

<main>
    <ul>
        {#each messages as message (message.id)}
            <li>{message.content}</li>
        {/each}
    </ul>

    <form on:submit|preventDefault={sendMessage}>
        <input bind:value={input} type="text" placeholder="Type a message..." />
        <button type="submit">Send</button>
    </form>
</main>
