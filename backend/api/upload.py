from fastapi import APIRouter, UploadFile, File
from backend.core.vector_db import VectorDatabase

router = APIRouter()
vector_db = VectorDatabase()

class UploadAPI:
    """Handles file uploads for SQL query storage."""

    @router.post("/upload_sql/")
    async def upload_sql(file: UploadFile = File(...)):
        contents = await file.read()
        queries = contents.decode().split(";")
        print(queries)
        for query in queries:
            vector_db.store_query(query.strip())

        return {"message": "SQL queries uploaded successfully"}
