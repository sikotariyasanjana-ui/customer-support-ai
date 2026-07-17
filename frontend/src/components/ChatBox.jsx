import { useState } from "react";
import axios from "axios";
import Message from "./Message";
import "../styles/chat.css";

function ChatBox() {

    const [messages, setMessages] = useState([]);
    const [text, setText] = useState("");

    const sendMessage = async () => {

        if (!text.trim()) return;

        const userMessage = {
            sender: "user",
            text: text,
        };

        setMessages((prev) => [...prev, userMessage]);

        try {

            const res = await axios.post(
                "http://127.0.0.1:8000/chat",
                {
                    message: text,
                }
            );

            const botMessage = {
                sender: "bot",
                text: res.data.response,
            };

            setMessages((prev) => [...prev, botMessage]);

        } catch (error) {

            setMessages((prev) => [
                ...prev,
                {
                    sender: "bot",
                    text: "Backend not running.",
                },
            ]);

        }

        setText("");

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
                />

                <button onClick={sendMessage}>
                    Send
                </button>

            </div>

        </div>

    );
}

export default ChatBox;