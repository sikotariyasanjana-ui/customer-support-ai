import { Link } from "react-router-dom";
import "../styles/navbar.css";

function Navbar() {
  return (
    <nav className="navbar">

      <div className="navbar-logo">

        <img
          src="/logo.png"
          alt="Customer Support AI"
          className="logo"
        />

        <h2>Customer Support AI</h2>

      </div>

      <ul className="navbar-menu">

        <li>
          <Link to="/">Home</Link>
        </li>

        <li>
          <Link to="/chat">Chat</Link>
        </li>

        <li>
          <Link to="/history">History</Link>
        </li>

        <li>
          <Link to="/settings">Settings</Link>
        </li>

        <li>
          <Link to="/login">Login</Link>
        </li>

        <li>
          <Link to="/register">Register</Link>
        </li>

      </ul>

    </nav>
  );
}

export default Navbar;