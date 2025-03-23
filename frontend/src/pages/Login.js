import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
const API_URL = "http://localhost:8000/auth"; // FastAPI Backend
import "../styles/Login.css"; 

const Login = () => {
    const [formData, setFormData] = useState({ username: "", password: "" });
    const [loading,setLoading]=useState(false);
    const navigate = useNavigate();
    

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try{
        const response = await fetch(`${API_URL}/login/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                username: formData.username,
                password: formData.password
            })
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data.user)
            localStorage.setItem("user", JSON.stringify(data.user));
            navigate("/");
        } else {
            alert("Invalid credentials");
        }
        setLoading(false);
    }catch(error){
        alert("Something went wrong. Please try again.");
    }
    };

    return (
        <div className="login-container">
            <h2>Login</h2>
            <form onSubmit={handleSubmit} className="login-form">
                <input type="text" name="username" placeholder="Username" onChange={handleChange} required />
                <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
                <button type="submit" disabled={loading}>
                {loading ? "Logging in..." : "Login"}
                </button>
            </form>
            
            {/* Register Button to Navigate to Register Page */}
            <p>Don't have an account?</p>
            <button onClick={() => navigate("/register")}>Register</button>

            {loading && (
                <div className="loading-overlay">
                    <div className="spinner"></div>
                    <p>Processing...</p>
                </div>
            )}
        </div>
    );
};

export default Login;
