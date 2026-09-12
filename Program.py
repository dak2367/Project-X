from User import User
from DatabaseManager import DatabaseManager
import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def main():
    db = DatabaseManager("Database.db")
    app = FastAPI()

    origins = [
    "http://localhost:5173",  # Default Vite + React port
    "http://localhost:3000",  # Default Create React App port
    ]

    # Add CORS middleware
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
    )

    @app.get("/api/data")
    async def get_data():
        return {"message": "Hello from FastAPI backend!"}