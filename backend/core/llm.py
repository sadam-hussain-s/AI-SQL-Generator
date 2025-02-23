import google.generativeai as genai
from backend.core.config import Config

class SQLGenerator:
    """Handles SQL query generation & optimization using Gemini API."""

    def __init__(self):
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-pro")  # Use correct model

    def generate_sql(self, user_prompt):
        response = self.model.generate_content(f"Convert this request into SQL which is suitable for Postgres: {user_prompt}")
        return response.text.strip() if response and response.text else "Failed to generate SQL"

    def optimize_sql(self, sql_query):
        response = self.model.generate_content(f"Optimize this SQL query: {sql_query}")
        return response.text.strip() if response and response.text else "Failed to optimize SQL"
