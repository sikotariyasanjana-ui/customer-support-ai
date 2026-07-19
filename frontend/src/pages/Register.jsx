import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { registerUser as apiRegisterUser } from "../services/authService";

function Register() {
    const navigate = useNavigate();

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState("");

    const handleRegister = async (e) => {
        e.preventDefault();
        setError("");
        setSuccess("");
        setLoading(true);

        try {
            await apiRegisterUser(name, email, password);
            setSuccess("Registration Successful! Redirecting to login...");
            setTimeout(() => {
                navigate("/login");
            }, 2000);
        } catch (err) {
            console.error("Registration failed:", err);
            setError(typeof err === "string" ? err : err.detail || "Registration failed. Try again.");
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
            <h2>Register</h2>

            {error && (
                <div style={{ color: "red", marginBottom: "15px", fontSize: "14px" }}>
                    ⚠️ {error}
                </div>
            )}

            {success && (
                <div style={{ color: "green", marginBottom: "15px", fontSize: "14px" }}>
                    ✅ {success}
                </div>
            )}

            <form onSubmit={handleRegister}>

                <input
                    placeholder="Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    disabled={loading}
                    required
                    style={{
                        width: "100%",
                        padding: "12px",
                        marginBottom: "15px",
                    }}
                />

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
                    {loading ? "Registering..." : "Register"}
                </button>

            </form>

            <br />

            <Link to="/login">
                Already have an account?
            </Link>

        </div>
    );
}

export default Register;