import { useState } from "react";

function MessageInput({ onSend }) {
    const [message, setMessage] = useState("");

    const handleSend = () => {
        if (!message.trim()) return;

        onSend(message);

        setMessage("");
    };

    return (
        <div
            style={{
                display: "flex",
                gap: "10px",
                padding: "15px",
                borderTop: "1px solid #ddd",
            }}
        >
            <input
                type="text"
                placeholder="Type your message..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyDown={(e) => {
                    if (e.key === "Enter") handleSend();
                }}
                style={{
                    flex: 1,
                    padding: "12px",
                    fontSize: "16px",
                }}
            />

            <button
                onClick={handleSend}
                style={{
                    padding: "12px 20px",
                    background: "#2563eb",
                    color: "white",
                    border: "none",
                    borderRadius: "5px",
                    cursor: "pointer",
                }}
            >
                Send
            </button>
        </div>
    );
}

export default MessageInput;