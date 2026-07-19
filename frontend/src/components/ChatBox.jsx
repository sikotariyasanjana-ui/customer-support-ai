import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import Message from "./Message";
import { sendMessage as sendChatMessage } from "../services/chatService";
import "../styles/chat.css";

function ChatBox() {
    const [searchParams] = useSearchParams();
    const agent = searchParams.get("agent") || "faq";

    const [messages, setMessages] = useState([]);
    const [text, setText] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSend = async () => {
        if (!text.trim()) return;

        const userMessage = {
            sender: "user",
            text: text,
        };

        setMessages((prev) => [...prev, userMessage]);
        const currentText = text;
        setText("");
        setLoading(true);

        try {
            const res = await sendChatMessage(currentText, agent);

            const botMessage = {
                sender: "bot",
                text: res.response,
            };

            setMessages((prev) => [...prev, botMessage]);

        } catch (error) {
            console.error("Chat Error:", error);
            setMessages((prev) => [
                ...prev,
                {
                    sender: "bot",
                    text: typeof error === "string" ? error : "Connection error. Make sure backend is running.",
                },
            ]);
        } finally {
            setLoading(false);
        }

    };

    return (

        <div className="chatbox">

            <div className="messages">

                {messages.map((msg, index) => (

                    <Message
                        key={index}
                        sender={msg.sender}
                        text={msg.text}
                    />

                ))}

            </div>

            <div className="chat-input">

                <input
                    type="text"
                    placeholder="Type your question..."
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") {
                            handleSend();
                        }
                    }}
                    disabled={loading}
                />

                <button onClick={handleSend} disabled={loading}>
                    {loading ? "Sending..." : "Send"}
                </button>

            </div>

        </div>

    );
}

export default ChatBox;