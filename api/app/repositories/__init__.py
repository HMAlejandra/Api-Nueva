"""
Repository layer for data access
"""
from api.app.repositories.artwork_repository import ArtworkRepository
from api.app.repositories.painting_repository import PaintingRepository

__all__ = ["ArtworkRepository", "PaintingRepository"]

