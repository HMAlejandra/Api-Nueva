"""
Service layer for managing artworks
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.artwork import Artwork
from app.repositories.artwork_repository import ArtworkRepository
from app.schemas.artwork import ArtworkCreate


class ArtworkService:
    """Service for artwork business logic"""
    
    def __init__(self, db: Session):
        self.repository = ArtworkRepository(db)
    
    def get_all_artworks(self) -> List[Artwork]:
        """Get all artworks"""
        return self.repository.find_all()
    
    def get_artwork_by_id(self, artwork_id: int) -> Optional[Artwork]:
        """Get artwork by ID"""
        return self.repository.find_by_id(artwork_id)
    
    def create_artwork(self, artwork_data: ArtworkCreate) -> Artwork:
        """Create a new artwork"""
        artwork = Artwork(
            code=artwork_data.code,
            title=artwork_data.title,
            author=artwork_data.author,
            description=artwork_data.description,
            image_url=artwork_data.image_url,
            type=artwork_data.type
        )
        return self.repository.save(artwork)
    
    def delete_artwork(self, artwork_id: int) -> None:
        """Delete an artwork"""
        self.repository.delete_by_id(artwork_id)

