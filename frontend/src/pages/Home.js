import React, { useState } from "react";
import QueryForm from "../components/QueryForm";
import QueryResult from "../components/QueryResult";
import FileUpload from "../components/FileUpload";

function Home() {
    const [result, setResult] = useState(null);


    return (
        <div>
            <QueryForm setResult={setResult} />
            <QueryResult result={result} />
            <FileUpload />
        </div>
    );
}

export default Home;
