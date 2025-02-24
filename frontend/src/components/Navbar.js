import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Navbar.css"; // Importing CSS from styles folder

const Navbar = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem("user");
        navigate("/login");
    };

    return (
        <nav className="navbar">
            <h2 className="logo">AI SQL Assistant</h2>
            <button className="logout-button" onClick={handleLogout}>Logout</button>
        </nav>
    );
};

export default Navbar;
