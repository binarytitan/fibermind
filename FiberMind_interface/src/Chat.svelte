<script>
    let messages = [];
    let input = '';

    async function sendMessage() {
        // TODO: Send message to server and update `messages`
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
