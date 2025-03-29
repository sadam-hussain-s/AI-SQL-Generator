import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import QueryForm from "../components/QueryForm";
import QueryResult from "../components/QueryResult";
import Navbar from "../components/Navbar";

function Home() {
    const [result, setResult] = useState(null);
    const navigate = useNavigate();

    return (
        <div>
            <Navbar />
            <QueryForm setResult={setResult} />
            <QueryResult result={result} />
        </div>
    );
}

export default Home;
