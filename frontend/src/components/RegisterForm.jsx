import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import LoadingIndicator from "./LoadingIndicator";
import "../styles/LoadingIndicator.css"


function RegisterForm() {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [first_name, setFirstName] = useState("")
    const [last_name, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault()

        try {
            const response = await api.post("/api/user/register/", {
                username,
                password,
                first_name,
                last_name,
                email
            });

            if (response.status === 201) {
                console.log("User registered successfully:", response.data);
                navigate("/login");
            } else {
                alert("Something went wrong. Please try again.");
            }
        } catch (error) {
            console.error(error);
            alert(error.response?.data?.detail || "Registration failed. Please try again.");
        } 
    };
            

    return (
    <form onSubmit={handleSubmit}>
        <h1>Register</h1>
        <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="username"
        />
        <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="password"
        />
        <input
            type="text"
            value={first_name}
            onChange={(e) => setFirstName(e.target.value)}
            placeholder="first-name"
        />
        <input
            type="text"
            value={last_name}
            onChange={(e) => setLastName(e.target.value)}
            placeholder="last-name"
        />
        <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="email"
        />
        {loading && <LoadingIndicator />}
        <button type="submit">
            Register
        </button>
    </form>
    );
}

export default RegisterForm