from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import query, upload, auth, performance_analyzer

app = FastAPI(title="GenAI SQL Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change to frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router, prefix="/api", tags=["SQL Generation"])
app.include_router(upload.router, prefix="/api", tags=["Uploads"])
app.include_router(performance_analyzer.router, prefix="/api", tags=["SQL Performance"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
async def root():
    return {"message": "Welcome to the GenAI SQL Assistant API"}