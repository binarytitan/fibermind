<script>
    let messages = [];
    let input = '';

    import { OpenAI } from 'openai';

    const openai = new OpenAI('your-openai-api-key');

    async function sendMessage() {
        messages.push({text: input, sender: 'user'});
        input = '';

        const gptResponse = await openai.complete({
            engine: 'gpt-3.5-turbo',
            prompt: messages.map(message => `${message.sender}: ${message.text}`).join('\n'),
            max_tokens: 60,
        });

        messages.push({text: gptResponse.data.choices[0].text.trim(), sender: 'bot'});
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
