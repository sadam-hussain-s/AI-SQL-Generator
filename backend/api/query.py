from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.core.llm import SQLGenerator

router = APIRouter()
sql_gen = SQLGenerator()

class QueryRequest(BaseModel):
    prompt: str

class SQLQueryRequest(BaseModel):
    sql_query: str

@router.post("/generate_sql/")
async def generate_sql(request: QueryRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")
    return {"sql_query": sql_gen.generate_sql(request.prompt)}

@router.post("/optimize_sql/")
async def optimize_sql(request: SQLQueryRequest):
    if not request.sql_query:
        raise HTTPException(status_code=400, detail="SQL query cannot be empty")
    
    optimized_query = sql_gen.optimize_sql(request.sql_query)
    return {"optimized_query": optimized_query}