import React, { useState } from "react";
import { uploadSQLFile } from "../api";
import "../styles/FileUpload.css"; 

function FileUpload() {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");
    const [loading,setLoading]=useState(false);

    const handleUpload = async () => {
        setLoading(true);
        if (!file) return;
        const formData = new FormData();
        formData.append("file", file);
        const data = await uploadSQLFile(formData);
        setMessage(data.message);
        setLoading(false);
    };

    return (
        <div className="upload-container">
            <h3>Upload SQL Query File (.sql)</h3>
            <input type="file" accept=".sql" onChange={(e) => setFile(e.target.files[0])}  />
            <button onClick={handleUpload} disabled={loading}>
            {loading ? "Uploading..." : "Upload"}
            </button>
            {message && <h3>{message}</h3>}

            {loading && (
                <div className="loading-overlay">
                    <div className="spinner"></div>
                    <p>Uploading...</p>
                </div>
            )}
        </div>
    );
}

export default FileUpload;
