from backend.core.vector_db import VectorDatabase
import google.generativeai as genai
from backend.core.config import Config

class SQLGenerator:
    """Handles SQL query generation & optimization using Gemini API."""

    def __init__(self):
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-pro")  # Use correct model
        self.vector_db = VectorDatabase()

    def generate_sql(self, user_prompt):
        similar_queries = self.vector_db.retrieve_similar_query(user_prompt)
        context = "\n".join(similar_queries) if similar_queries else ""
        prompt = f"""Given these example queries:\n{context}\nBased on this request, generate an 
        optimized SQL query for Postgres : {user_prompt}"""
    
        response = self.model.generate_content(prompt)
        generated_sql=""
        if response and response.text:
            generated_sql=response.text.strip()
            self.vector_db.store_query(generated_sql)
        else:
            generated_sql="Failed to generate SQL" 
        return generated_sql

    def optimize_sql(self, sql_query):
        response = self.model.generate_content(f"Optimize this SQL query: {sql_query}")
        return response.text.strip() if response and response.text else "Failed to optimize SQL"
