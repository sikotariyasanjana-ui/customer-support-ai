import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Register() {
    const navigate = useNavigate();

    const [name, setName] = useState("");

    const [email, setEmail] = useState("");

    const [password, setPassword] = useState("");

    const registerUser = (e) => {
        e.preventDefault();

        alert("Registration Successful");

        navigate("/login");
    };

    return (
        <div
            style={{
                width: "400px",
                margin: "80px auto",
            }}
        >
            <h2>Register</h2>

            <form onSubmit={registerUser}>

                <input
                    placeholder="Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    style={{
                        width: "100%",
                        padding: "12px",
                        marginBottom: "15px",
                    }}
                />

                <input
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
                    Register
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