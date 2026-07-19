import { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar";
import { getChatHistory, clearHistory } from "../services/chatService";
import "../styles/history.css";

function History() {
    const [chats, setChats] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const fetchHistory = async () => {
        setLoading(true);
        setError("");
        try {
            const data = await getChatHistory();
            setChats(data);
        } catch (err) {
            console.error("Failed to load chat history:", err);
            setError("Could not load chat history. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchHistory();
    }, []);

    const handleClear = async () => {
        if (!window.confirm("Are you sure you want to clear your chat history?")) return;
        try {
            await clearHistory();
            setChats([]);
        } catch (err) {
            console.error("Failed to clear chat history:", err);
            alert("Failed to clear chat history.");
        }
    };

    return (
        <div className="history-page">
            <Sidebar />

            <div className="history-content">
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "20px" }}>
                    <h1>📜 Chat History</h1>
                    {chats.length > 0 && (
                        <button 
                            onClick={handleClear}
                            style={{
                                padding: "8px 16px",
                                backgroundColor: "#ff4d4d",
                                color: "white",
                                border: "none",
                                borderRadius: "4px",
                                cursor: "pointer",
                                fontSize: "14px"
                            }}
                        >
                            Clear All
                        </button>
                    )}
                </div>

                {loading && <p>Loading history...</p>}
                {error && <p style={{ color: "red" }}>{error}</p>}

                {!loading && chats.length === 0 && (
                    <p style={{ color: "#666", fontStyle: "italic" }}>No chat history found.</p>
                )}

                {!loading && chats.map((chat) => (
                    <div className="history-card" key={chat.id}>
                        <h3>{chat.agent}</h3>

                        <p>
                            <strong>Question:</strong> {chat.question}
                        </p>

                        <p>
                            <strong>Answer:</strong> {chat.answer}
                        </p>

                        {chat.timestamp && (
                            <div style={{ fontSize: "11px", color: "#888", marginTop: "10px", textAlign: "right" }}>
                                {new Date(chat.timestamp).toLocaleString()}
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default History;