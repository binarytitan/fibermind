<script>
    let messages = [];
    let input = '';

    async function sendMessage() {
        messages.push({text: input, sender: 'user'});
        input = '';

        const res = await fetch('http://localhost:5000/message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({messages})
        });
        const data = await res.json();

        messages.push({text: data.message, sender: 'bot'});
    }
</script>

<style>
    /* Add your styles here */
</style>

<div>
    <div>
        {#each messages as message (message.text)}
            <div>
                <strong>{message.sender}:</strong> {message.text}
            </div>
        {/each}
    </div>
    <div>
        <input bind:value={input} on:keydown|preventDefault="Enter"={sendMessage}>
        <button on:click={sendMessage}>Send</button>
    </div>
</div>
