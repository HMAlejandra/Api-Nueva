"""
Router for emotion-based operations
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.emotion import EmotionRequest, EmotionResponse
from app.services.emotion_service import EmotionService

router = APIRouter(prefix="/api/obra", tags=["obra"])


@router.post("/emocion", response_model=EmotionResponse, status_code=status.HTTP_200_OK)
async def post_emotion(request: EmotionRequest, db: Session = Depends(get_db)):
    """
    Generate emotion-based comment for an artwork

    Args:
        request: Emotion request with estado_animo and obra_id
        db: Database session

    Returns:
        Emotion response with comentario
    """
    service = EmotionService(db)
    return await service.generar_comentario(request)

