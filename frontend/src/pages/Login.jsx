import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

function Login() {
    const navigate = useNavigate();

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const handleLogin = (e) => {
        e.preventDefault();

        localStorage.setItem("token", "demo-token");

        navigate("/");
    };

    return (
        <div
            style={{
                width: "400px",
                margin: "80px auto",
            }}
        >
            <h2>Login</h2>

            <form onSubmit={handleLogin}>

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "12px",
                        marginBottom: "15px",
                    }}
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "12px",
                        marginBottom: "15px",
                    }}
                />

                <button
                    style={{
                        width: "100%",
                        padding: "12px",
                    }}
                >
                    Login
                </button>

            </form>

            <br />

            <Link to="/register">
                Create Account
            </Link>

        </div>
    );
}

export default Login;