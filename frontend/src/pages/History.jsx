import Sidebar from "../components/Sidebar";
import "../styles/history.css";

function History() {
    const chats = [
        {
            id: 1,
            agent: "Billing Agent",
            question: "How do I get my invoice?",
            answer: "You can download your invoice from your account dashboard."
        },
        {
            id: 2,
            agent: "Technical Agent",
            question: "My application is not opening.",
            answer: "Please restart the application and check your internet connection."
        },
        {
            id: 3,
            agent: "FAQ Agent",
            question: "What are your support hours?",
            answer: "Customer Support AI is available 24×7."
        }
    ];

    return (
        <div className="history-page">
            <Sidebar />

            <div className="history-content">
                <h1>📜 Chat History</h1>

                {chats.map((chat) => (
                    <div className="history-card" key={chat.id}>
                        <h3>{chat.agent}</h3>

                        <p>
                            <strong>Question:</strong> {chat.question}
                        </p>

                        <p>
                            <strong>Answer:</strong> {chat.answer}
                        </p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default History;