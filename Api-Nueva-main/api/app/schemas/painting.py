"""
Pydantic schemas for Painting
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional


class PaintingBase(BaseModel):
    code: Optional[str] = None
    title: Optional[str] = None
    artist: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    category: Optional[str] = None


class PaintingCreate(PaintingBase):
    """Schema for creating a painting"""
    pass


class PaintingResponse(PaintingBase):
    """Schema for painting response"""
    id: int
    
    model_config = ConfigDict(from_attributes=True)

