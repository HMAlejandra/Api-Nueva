"""
Router for painting operations
"""

from typing import List
from fastapi import APIRouter, HTTPException, status, Body
from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.painting import PaintingCreate, PaintingResponse
from app.services.painting_service import PaintingService
from app.services.gemini_service import GeminiService

router = APIRouter(prefix="/paintings", tags=["paintings"])

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


@router.post("/{painting_id}/comment")
async def generate_comment(painting_id: int, mood: str = Body(..., embed=True), db: Session = Depends(get_db)):
    """Generate a comment for a painting based on mood using Gemini"""
    service = PaintingService(db)
    painting = service.get_painting_by_id(painting_id)
    if not painting:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Painting with id {painting_id} not found"
        )
    gemini_service = GeminiService()
    ai_comment = gemini_service.generate_comment(mood, painting.title)
    return {
        "painting_id": painting_id,
        "title": painting.title,
        "mood": mood,
        "ai_comment": ai_comment
    }