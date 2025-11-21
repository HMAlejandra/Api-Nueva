"""
Main FastAPI application
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base
from app.routers import artworks, paintings, gemini, emotions, health, root, user
from app.models.user import User
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup and shutdown events
    """
    # Startup: Create tables and load initial data
    Base.metadata.create_all(bind=engine)
    import app.config.data_loader as data_loader
    data_loader.init_data()
    yield
    # Shutdown: Cleanup if needed
    pass


# Create FastAPI app
app = FastAPI(
    title="SoulTrip Backend API",
    description="FastAPI backend for museum management system",
    version="0.1.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

# Include routers
app.include_router(root.router)
app.include_router(health.router)
app.include_router(artworks.router)
app.include_router(paintings.router)
app.include_router(gemini.router)
app.include_router(emotions.router)
app.include_router(user.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )

