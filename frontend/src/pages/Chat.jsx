import Sidebar from "../components/Sidebar";
import ChatBox from "../components/ChatBox";
import "../styles/chat.css";

function Chat() {
  return (
    <div className="chat-page">

      <Sidebar />

      <div className="chat-content">

        <div className="chat-header">
          <h1>🤖 Customer Support AI</h1>
          <p>Ask anything about Billing, Products, Technical Support, Complaints or FAQs.</p>
        </div>

        <ChatBox />

      </div>

    </div>
  );
}

export default Chat;