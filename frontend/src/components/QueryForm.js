import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { generateSQL, optimizeSQL } from "../api";

function QueryForm({ setResult }) {
    const [query, setQuery] = useState("");
    const navigate = useNavigate();
    
    const handleGenerate = async () => {
        const data = await generateSQL(query);
        console.log("Generated SQL Response:", data); // ✅ Debug log
        setResult(data);
    };

    const handleOptimize = async () => {
        const data = await optimizeSQL({ sql_query: query });  // ✅ Wrap query inside an object
        console.log("Optimized SQL Response:", data); // ✅ Debug log
        setResult(data);
    };

    const handleUpload = async () => {
        navigate("/upload");
    };

    return (
        <div className="container">
            <h2>AI SQL Assistant</h2>
            <textarea
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter natural language query..."
            />
            <button onClick={handleGenerate}>Generate SQL</button>
            <button onClick={handleOptimize}>Optimize SQL</button>
            <button onClick={handleUpload}>Upload your SQL Queries</button>
        </div>
    );
}

export default QueryForm;
