"""
Service layer for managing paintings
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from app.models import Painting

class PaintingService:
    """Service for painting business logic"""

    def __init__(self, db: Session):
        self.db = db

    def get_all_paintings(self) -> List[Painting]:
        """Get all paintings"""
        return self.db.query(Painting).all()

    def get_painting_by_id(self, painting_id: int) -> Optional[Painting]:
        """Get painting by ID"""
        return self.db.query(Painting).filter(Painting.id == painting_id).first()

    def create_painting(self, painting_data) -> Painting:
        """Create a new painting"""
        painting = Painting(
            title=painting_data.title,
            image_url=painting_data.image_url
        )
        self.db.add(painting)
        self.db.commit()
        self.db.refresh(painting)
        return painting

    def delete_painting(self, painting_id: int) -> None:
        """Delete a painting"""
        painting = self.get_painting_by_id(painting_id)
        if painting:
            self.db.delete(painting)
            self.db.commit()