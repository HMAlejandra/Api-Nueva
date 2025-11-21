"""
Service layer for managing paintings
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.painting import Painting
from app.repositories.painting_repository import PaintingRepository
from app.schemas.painting import PaintingCreate


class PaintingService:
    """Service for painting business logic"""
    
    def __init__(self, db: Session):
        self.repository = PaintingRepository(db)
    
    def get_all_paintings(self) -> List[Painting]:
        """Get all paintings"""
        return self.repository.find_all()
    
    def get_painting_by_id(self, painting_id: int) -> Optional[Painting]:
        """Get painting by ID"""
        return self.repository.find_by_id(painting_id)
    
    def create_painting(self, painting_data: PaintingCreate) -> Painting:
        """Create a new painting"""
        painting = Painting(
            code=painting_data.code,
            title=painting_data.title,
            artist=painting_data.artist,
            description=painting_data.description,
            image_url=painting_data.image_url,
            category=painting_data.category
        )
        return self.repository.save(painting)
    
    def delete_painting(self, painting_id: int) -> None:
        """Delete a painting"""
        self.repository.delete_by_id(painting_id)

