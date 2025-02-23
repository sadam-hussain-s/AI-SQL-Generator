import psycopg2
from sentence_transformers import SentenceTransformer
import numpy as np
from backend.core.config import Config
import datetime

class VectorDatabase:
    """Handles storing & retrieving SQL embeddings using pgvector."""

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=Config.VECTOR_DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            host=Config.DB_HOST,
            port=Config.DB_PORT
        )
        self.cur = self.conn.cursor()
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS sql_queries (
                id SERIAL PRIMARY KEY,
                query TEXT NOT NULL,
                embedding VECTOR(384),
                created timestamp
            );
        """)
        self.conn.commit()

    def store_query(self, query_text):
        embedding = self.model.encode([query_text])[0].tolist()
        embedding_str = f"ARRAY{embedding}"
        self.cur.execute("INSERT INTO sql_queries (query, embedding, created) VALUES (%s, %s::vector, %s::timestamp)", 
                        (query_text, embedding, datetime.datetime.now()))
        self.conn.commit()

    def retrieve_similar_query(self, input_query):
        embedding = self.model.encode([input_query])[0].tolist()
        embedding_str = f"ARRAY{embedding}"
        self.cur.execute("""
            SELECT query FROM sql_queries 
            ORDER BY embedding <-> %s::vector 
            LIMIT 1;
        """, (embedding,))
        return self.cur.fetchone()
