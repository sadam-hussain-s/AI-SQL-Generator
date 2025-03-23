import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
const API_URL = "http://localhost:8000/auth"; // FastAPI Backend
import "../styles/Register.css"; 

const Register = () => {
    const [formData, setFormData] = useState({ username: "", email: "", password: "" });
    const [loading,setLoading]=useState(false);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try{
        const response = await fetch(`${API_URL}/register/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                username: formData.username,
                email: formData.email,
                password: formData.password
            }),
        });

        if (response.ok) {
            alert("Registration successful! Please login.");
            navigate("/login");
        } else {
            alert("Registration failed. Try a different username/email.");
        }
        setLoading(false);
    }catch(error){
        alert("Something went wrong. Please try again.");
    }
    };

    return (
        <div className="register-container">
        <form onSubmit={handleSubmit} className="register-form">
            <input type="text" name="username" placeholder="Username" onChange={handleChange} required />
            <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
            <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
            <button type="submit" disabled={loading}>
            {loading ? "Registering..." : "Register"}
            </button>
        </form>
        {loading && (
                <div className="loading-overlay">
                    <div className="spinner"></div>
                    <p>Processing...</p>
                </div>
            )}
        </div>
    );
};

export default Register;
