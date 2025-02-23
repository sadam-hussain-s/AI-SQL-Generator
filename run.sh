#!/bin/bash

# Start FastAPI backend
echo "Starting backend..."
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Start React frontend
echo "Starting frontend..."
cd frontend
npm start
