"""
Repository layer for data access
"""
from app.repositories.artwork_repository import ArtworkRepository
from app.repositories.painting_repository import PaintingRepository

__all__ = ["ArtworkRepository", "PaintingRepository"]

