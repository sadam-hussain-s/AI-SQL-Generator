import React from "react";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        localStorage.removeItem("user");
        navigate("/login");
    };

    return (
        <nav>
            <h2>AI SQL Assistant</h2>
            <button onClick={handleLogout}>Logout</button>
        </nav>
    );
};

export default Navbar;
