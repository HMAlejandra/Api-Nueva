"""
Router for painting operations
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.painting import PaintingCreate, PaintingResponse
from app.services.painting_service import PaintingService

router = APIRouter(prefix="/api/paintings", tags=["paintings"])


@router.get("", response_model=List[PaintingResponse])
async def get_all_paintings(db: Session = Depends(get_db)):
    """Get all paintings"""
    service = PaintingService(db)
    return service.get_all_paintings()


@router.get("/{painting_id}", response_model=PaintingResponse)
async def get_painting_by_id(painting_id: int, db: Session = Depends(get_db)):
    """Get painting by ID"""
    service = PaintingService(db)
    painting = service.get_painting_by_id(painting_id)
    if not painting:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Painting with id {painting_id} not found"
        )
    return painting


@router.post("", response_model=PaintingResponse, status_code=status.HTTP_201_CREATED)
async def create_painting(painting_data: PaintingCreate, db: Session = Depends(get_db)):
    """Create a new painting"""
    service = PaintingService(db)
    return service.create_painting(painting_data)


@router.delete("/{painting_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_painting(painting_id: int, db: Session = Depends(get_db)):
    """Delete a painting"""
    service = PaintingService(db)
    painting = service.get_painting_by_id(painting_id)
    if not painting:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Painting with id {painting_id} not found"
        )
    service.delete_painting(painting_id)

