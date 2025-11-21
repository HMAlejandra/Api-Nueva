from pydantic import BaseModel
from typing import Optional

class PaintingBase(BaseModel):
    title: str
    image_url: str

class PaintingCreate(PaintingBase):
    pass

class PaintingResponse(PaintingBase):
    id: int

    class Config:
        from_attributes = True