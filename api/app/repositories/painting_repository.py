"""
Repository for managing paintings
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from api.app.models.painting import Painting


class PaintingRepository:
    """Repository for painting data access operations"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def find_all(self) -> List[Painting]:
        """Get all paintings"""
        return self.db.query(Painting).all()
    
    def find_by_id(self, painting_id: int) -> Optional[Painting]:
        """Get painting by ID"""
        return self.db.query(Painting).filter(Painting.id == painting_id).first()
    
    def save(self, painting: Painting) -> Painting:
        """Save or update a painting"""
        self.db.add(painting)
        self.db.commit()
        self.db.refresh(painting)
        return painting
    
    def delete_by_id(self, painting_id: int) -> None:
        """Delete painting by ID"""
        painting = self.find_by_id(painting_id)
        if painting:
            self.db.delete(painting)
            self.db.commit()

    # 🚀 MÉTODO QUE TE FALTABA
    def count(self) -> int:
        """Return total number of rows in paintings table"""
        return self.db.query(Painting).count()
