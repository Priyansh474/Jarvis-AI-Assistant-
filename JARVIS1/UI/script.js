async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatBox = document.getElementById('chatBox');
    const query = userInput.value;

    // Add user message to chat
    chatBox.innerHTML += `<p><strong>You:</strong> ${query}</p>`;
    userInput.value = '';

    try {
        const response = await fetch('http://localhost:8000/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query })
        });

        const data = await response.json();
        chatBox.innerHTML += `<p><strong>Assistant:</strong> ${data.response}</p>`;
    } catch (error) {
        console.error('Error:', error);
        chatBox.innerHTML += `<p><strong>Error:</strong> Failed to get response</p>`;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

// Handle Enter key press
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});