"""
Pydantic schemas for Emotion endpoints
"""
from pydantic import BaseModel


class EmotionRequest(BaseModel):
    """Request schema for emotion endpoint"""
    estado_animo: str
    obra_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "estado_animo": "feliz",
                "obra_id": 1
            }
        }


class EmotionResponse(BaseModel):
    """Response schema for emotion endpoint"""
    obra_id: int
    comentario: str

