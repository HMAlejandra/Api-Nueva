"""
Router for artwork operations
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.artwork import ArtworkCreate, ArtworkResponse
from app.services.artwork_service import ArtworkService

router = APIRouter(prefix="/api/artworks", tags=["artworks"])


@router.get("", response_model=List[ArtworkResponse])
async def get_all_artworks(db: Session = Depends(get_db)):
    """Get all artworks"""
    service = ArtworkService(db)
    return service.get_all_artworks()


@router.get("/{artwork_id}", response_model=ArtworkResponse)
async def get_artwork_by_id(artwork_id: int, db: Session = Depends(get_db)):
    """Get artwork by ID"""
    service = ArtworkService(db)
    artwork = service.get_artwork_by_id(artwork_id)
    if not artwork:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Artwork with id {artwork_id} not found"
        )
    return artwork


@router.post("", response_model=ArtworkResponse, status_code=status.HTTP_201_CREATED)
async def create_artwork(artwork_data: ArtworkCreate, db: Session = Depends(get_db)):
    """Create a new artwork"""
    service = ArtworkService(db)
    return service.create_artwork(artwork_data)


@router.delete("/{artwork_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_artwork(artwork_id: int, db: Session = Depends(get_db)):
    """Delete an artwork"""
    service = ArtworkService(db)
    artwork = service.get_artwork_by_id(artwork_id)
    if not artwork:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Artwork with id {artwork_id} not found"
        )
    service.delete_artwork(artwork_id)

