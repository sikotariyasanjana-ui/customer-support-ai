import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { loginUser } from "../services/authService";

function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleLogin = async (e) => {
        e.preventDefault();
        setError("");
        setLoading(true);

        try {
            await loginUser(email, password);
            navigate("/");
        } catch (err) {
            console.error("Login failed:", err);
            setError(typeof err === "string" ? err : err.detail || "Invalid email or password.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div
            style={{
                width: "400px",
                margin: "80px auto",
            }}
        >
            <h2>Login</h2>

            {error && (
                <div style={{ color: "red", marginBottom: "15px", fontSize: "14px" }}>
                    ⚠️ {error}
                </div>
            )}

            <form onSubmit={handleLogin}>

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    disabled={loading}
                    required
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
                    disabled={loading}
                    required
                    style={{
                        width: "100%",
                        padding: "12px",
                        marginBottom: "15px",
                    }}
                />

                <button
                    type="submit"
                    disabled={loading}
                    style={{
                        width: "100%",
                        padding: "12px",
                        cursor: loading ? "not-allowed" : "pointer"
                    }}
                >
                    {loading ? "Logging in..." : "Login"}
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