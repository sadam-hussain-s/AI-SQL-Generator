'''import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
VECTOR_DB_URL=os.getenv("VECTOR_DB_URL")
'''

import os
from dotenv import load_dotenv

class Config:
    """Loads and stores environment configurations."""
    
    load_dotenv()
    
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    VECTOR_DB_NAME = os.getenv("VECTOR_DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
