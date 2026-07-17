import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import App from "./App";

import "./styles/app.css";
import "./styles/navbar.css";
import "./styles/sidebar.css";
import "./styles/home.css";
import "./styles/chat.css";
import "./styles/history.css";
import "./styles/login.css";
import "./styles/register.css";
import "./styles/settings.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);