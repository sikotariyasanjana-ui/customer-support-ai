import { useState } from "react";
import Sidebar from "../components/Sidebar";
import "../styles/settings.css";

function Settings() {
    const [theme, setTheme] = useState("Light");
    const [notifications, setNotifications] = useState(true);
    const [aiModel, setAiModel] = useState("Gemini 2.5 Flash");

    const saveSettings = () => {
        alert("Settings Saved Successfully!");
    };

    return (
        <div className="settings-layout">
            <Sidebar />

            <div className="settings-container">
                <h1>⚙ Settings</h1>

                <div className="settings-card">

                    <div className="setting-item">
                        <label>Theme</label>

                        <select
                            value={theme}
                            onChange={(e) => setTheme(e.target.value)}
                        >
                            <option>Light</option>
                            <option>Dark</option>
                        </select>
                    </div>

                    <div className="setting-item">
                        <label>AI Model</label>

                        <select
                            value={aiModel}
                            onChange={(e) => setAiModel(e.target.value)}
                        >
                            <option>Gemini 2.5 Flash</option>
                            <option>Gemini 2.5 Pro</option>
                        </select>
                    </div>

                    <div className="setting-item">
                        <label>Notifications</label>

                        <input
                            type="checkbox"
                            checked={notifications}
                            onChange={() => setNotifications(!notifications)}
                        />
                    </div>

                    <button onClick={saveSettings}>
                        Save Settings
                    </button>

                </div>
            </div>
        </div>
    );
}

export default Settings;