import React from "react";

function QueryResult({ result }) {
    return (
        <div className="container">
            <h3>Generated SQL Query:</h3>
            <pre>{result?.sql_query || result?.optimized_query || "No query generated yet"}</pre>
        </div>
    );
}

export default QueryResult;
