import React from "react";
import "../styles/QueryResult.css";

function QueryResult({ result }) {
    
    const sqlQuery = result?.sql_query || result?.optimized_query || "No query generated yet";

    // Properly replace the first and last triple quotes
    const formattedQuery = sqlQuery.replace(/```([\s\S]*?)```/g, '<div class="code-block">$1</div>').replace(/\*\*(.*?)\*\*/g, '<b>$1</b>');

    return (
        <div className="markdown-content">
            <h3>Generated SQL Query:</h3>
            <div dangerouslySetInnerHTML={{ __html: formattedQuery }} />
        </div>
    );
}

export default QueryResult;
