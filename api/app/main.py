"""
Main FastAPI application
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.app.config import settings
from api.app.database import engine, Base
from api.app.routers import paintings, gemini, emotions, root
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup and shutdown events
    """
    Base.metadata.create_all(bind=engine)
    import api.app.config.data_loader as data_loader
    data_loader.init_data()
    yield
    pass


app = FastAPI(
    title="SoulTrip Backend API",
    description="FastAPI backend for museum management system",
    version="0.1.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

# Include routers
app.include_router(root.router)
app.include_router(paintings.router)
app.include_router(gemini.router)
app.include_router(emotions.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=False
    )
