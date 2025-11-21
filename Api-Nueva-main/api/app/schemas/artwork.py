"""
Pydantic schemas for Artwork
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional


class ArtworkBase(BaseModel):
    code: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    type: Optional[str] = None


class ArtworkCreate(ArtworkBase):
    """Schema for creating an artwork"""
    pass


class ArtworkResponse(ArtworkBase):
    """Schema for artwork response"""
    id: int
    
    model_config = ConfigDict(from_attributes=True)

