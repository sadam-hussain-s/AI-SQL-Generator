from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.core.llm import SQLGenerator
from backend.core.performance import SQLPerformanceAnalyzer
from backend import logger

router = APIRouter()
sql_gen = SQLGenerator()
sql_analyzer = SQLPerformanceAnalyzer()


class SQLQueryRequest(BaseModel):
    sql_query: str


@router.post("/analyze_sql/")
async def analyze_sql(request: SQLQueryRequest):
    logger.info("inside analyze sql")
    logger.info(f"Received request:{ request.dict()}")
    if not request.sql_query:
        raise HTTPException(status_code=400, detail="SQL query cannot be empty")
    
    logger.info(f"Executing SQL: {request.sql_query}")
    execution_time = sql_analyzer.analyze_query(request.sql_query)
    optimized_query = sql_gen.optimize_sql(request.sql_query)
    logger.info(f"Execution time: {execution_time}") 

    return {
        "execution_time": execution_time,
        "optimized_query": optimized_query
    }