"""
Repository for managing artworks
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.artwork import Artwork


class ArtworkRepository:
    """Repository for artwork data access operations"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def find_all(self) -> List[Artwork]:
        """Get all artworks"""
        return self.db.query(Artwork).all()
    
    def find_by_id(self, artwork_id: int) -> Optional[Artwork]:
        """Get artwork by ID"""
        return self.db.query(Artwork).filter(Artwork.id == artwork_id).first()
    
    def save(self, artwork: Artwork) -> Artwork:
        """Save or update an artwork"""
        self.db.add(artwork)
        self.db.commit()
        self.db.refresh(artwork)
        return artwork
    
    def delete_by_id(self, artwork_id: int) -> None:
        """Delete artwork by ID"""
        artwork = self.find_by_id(artwork_id)
        if artwork:
            self.db.delete(artwork)
            self.db.commit()
    
    def count(self) -> int:
        """Count total artworks"""
        return self.db.query(Artwork).count()

