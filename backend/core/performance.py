import time
import psycopg2
from backend import logger
from backend.core.config import Config


class SQLPerformanceAnalyzer:
    """Analyzes query performance & suggests optimizations."""

    def __init__(self):
        logger.info("Initializing SQLPerformanceAnalyzer...")
        try:
            DATABASE_URL = Config.PROD_DATABASE_URL
            self.conn = psycopg2.connect(DATABASE_URL)
            self.cur = self.conn.cursor()
        except Exception as e:
            logger.error(f"Database connection failed: {str(e)}")
            self.conn = None
            self.cur = None

    def analyze_query(self, sql_query):
        """Executes the SQL query and measures execution time."""
        if not self.conn or not self.cur:
            return "Database connection not available"

        try:
            start_time = time.time()
            self.cur.execute(sql_query)
            execution_time = (time.time() - start_time) * 1000
            return "Time taken is: "+str(round(execution_time, 2)) + " ms"
        
        except Exception as e:
            logger.error(f"Query execution failed: {str(e)}")
            return f"Error: {str(e)}"
