import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { analyzeSQLPerformance, generateSQL, optimizeSQL } from "../api";
import "../styles/QueryForm.css"; 

function QueryForm({ setResult }) {
    const [query, setQuery] = useState("");
    const navigate = useNavigate();
    const [loading,setLoading]=useState(false);
    
    const handleGenerate = async () => {
        setLoading(true);
        const data = await generateSQL(query);
        console.log("Generated SQL Response:", data); // ✅ Debug log
        setResult(data);
        setLoading(false);
    };

    const handleOptimize = async () => {
        setLoading(true);
        const data = await optimizeSQL({ sql_query: query });  // ✅ Wrap query inside an object
        console.log("Optimized SQL Response:", data); // ✅ Debug log
        setResult(data);
        setLoading(false);
    };

    const handleUpload = async () => {
        navigate("/upload");
    };

    const handleAnalyze = async () => {
        setLoading(true);
        const data = await analyzeSQLPerformance({ sql_query: query });  // ✅ Wrap query inside an object
        console.log("Optimized SQL Response:", data); // ✅ Debug log
        setResult(data);
        setLoading(false);
    };

    return (
        <div className="query-container">
            <h2>AI SQL Assistant</h2>
            <textarea
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Enter natural language query / SQL query..."
            />
            <button onClick={handleGenerate} disabled={loading}>Generate SQL</button>
            <button onClick={handleOptimize} disabled={loading}>Optimize SQL</button>
            <button onClick={handleAnalyze} disabled={loading}>Analyze SQL</button>
            <button onClick={handleUpload} disabled={loading}>Upload your SQL Queries</button>
            {loading && (
                <div className="loading-overlay">
                    <div className="spinner"></div>
                    <p>Processing...</p>
                </div>
            )}
        </div>
    );
}

export default QueryForm;
