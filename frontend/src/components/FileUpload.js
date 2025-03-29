import React, { useState } from "react";
import { uploadSQLFile } from "../api";

function FileUpload() {
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");

    const handleUpload = async () => {
        if (!file) return;
        const formData = new FormData();
        formData.append("file", file);
        const data = await uploadSQLFile(formData);
        setMessage(data.message);
    };

    return (
        <div className="container">
            <h3>Upload SQL Query File (.sql)</h3>
            <input type="file" accept=".sql" onChange={(e) => setFile(e.target.files[0])}  />
            <button onClick={handleUpload}>Upload</button>
            {message && <p>{message}</p>}
        </div>
    );
}

export default FileUpload;
