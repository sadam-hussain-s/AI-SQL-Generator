const API_URL = "http://localhost:8000/api"; // FastAPI Backend

export async function generateSQL(prompt) {
    const response = await fetch(`${API_URL}/generate_sql/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
    });
    return response.json();
}

export async function optimizeSQL(query) {
    const response = await fetch(`${API_URL}/optimize_sql/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify( query ),
    });
    return response.json();
}

export async function uploadSQLFile(formData) {
    const response = await fetch(`${API_URL}/upload_sql/`, {
        method: "POST",
        body: formData,
    });
    return response.json();
}

export async function analyzeSQLPerformance(query) {
    const response = await fetch(`${API_URL}/analyze_sql/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify( query ),
    });
    return response.json();
}
