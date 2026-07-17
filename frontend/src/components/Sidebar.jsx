import { NavLink } from "react-router-dom";
import "../styles/sidebar.css";

function Sidebar() {
    return (
        <aside className="sidebar">

            <div className="sidebar-title">
                <h2>AI Agents</h2>
            </div>

            <nav className="sidebar-menu">

                <NavLink to="/" className="menu-item">
                    🏠 Dashboard
                </NavLink>

                <NavLink to="/chat" className="menu-item">
                    💬 AI Chat
                </NavLink>

                <NavLink to="/history" className="menu-item">
                    📜 History
                </NavLink>

                <NavLink to="/settings" className="menu-item">
                    ⚙️ Settings
                </NavLink>

                <hr />

                <h3 className="agent-heading">Support Agents</h3>

                <NavLink to="/chat?agent=billing" className="menu-item">
                    💳 Billing Agent
                </NavLink>

                <NavLink to="/chat?agent=technical" className="menu-item">
                    🛠 Technical Agent
                </NavLink>

                <NavLink to="/chat?agent=product" className="menu-item">
                    📦 Product Agent
                </NavLink>

                <NavLink to="/chat?agent=complaint" className="menu-item">
                    ⚠ Complaint Agent
                </NavLink>

                <NavLink to="/chat?agent=faq" className="menu-item">
                    ❓ FAQ Agent
                </NavLink>

            </nav>

        </aside>
    );
}

export default Sidebar;