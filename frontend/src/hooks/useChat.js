import { useState } from "react";

function useChat() {
    const [messages, setMessages] = useState([
        {
            sender: "AI",
            text: "Hello! How can I help you today?",
        },
    ]);

    const sendMessage = (text) => {
        if (!text.trim()) return;

        const userMessage = {
            sender: "You",
            text,
        };

        setMessages((prev) => [...prev, userMessage]);

        // Demo AI response
        setTimeout(() => {
            const aiMessage = {
                sender: "AI",
                text: "This is a demo AI response. Later it will come from your FastAPI backend.",
            };

            setMessages((prev) => [...prev, aiMessage]);
        }, 1000);
    };

    return {
        messages,
        sendMessage,
    };
}

export default useChat;