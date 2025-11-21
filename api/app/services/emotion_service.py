"""
Service for emotion-based painting recommendations
"""

from typing import Optional
from sqlalchemy.orm import Session

from api.app.schemas.emotion import EmotionRequest, EmotionResponse
from api.app.repositories.painting_repository import PaintingRepository
from api.app.services.gemini_service import GeminiService
from api.app.config import settings


class EmotionService:
    """Service for generating emotion-based comments for paintings"""

    def __init__(self, db: Session):
        self.painting_repository = PaintingRepository(db)
        self.gemini_service = GeminiService()

    async def generar_comentario(self, request: EmotionRequest) -> EmotionResponse:
        """
        Generate a comment based on user's emotional state and selected painting.

        Args:
            request: Emotion request with estado_animo and obra_id

        Returns:
            EmotionResponse with comentario
        """

        # Get painting from DB
        painting = self.painting_repository.find_by_id(request.obra_id)

        if not painting:
            fallback = (
                f"Tu estado es '{request.estado_animo}', pero no encontré la obra solicitada. "
                "Respira profundo y observa cómo el arte puede ayudarte a conectar contigo."
            )
            return EmotionResponse(obra_id=request.obra_id, comentario=fallback)

        # Build Gemini prompt
        prompt = self._build_prompt(request.estado_animo, painting)

        # Validate Gemini config
        if not settings.gemini_endpoint or not settings.gemini_api_key:
            fallback = (
                f"Sobre tu estado '{request.estado_animo}' y la obra '{painting.title}': "
                "el arte siempre puede acompañarte. Observa los detalles y deja que te inspire."
            )
            return EmotionResponse(obra_id=request.obra_id, comentario=fallback)

        # Call Gemini service
        try:
            comentario = await self.gemini_service.generar_comentario(prompt)
            return EmotionResponse(obra_id=request.obra_id, comentario=comentario)

        except Exception as e:
            fallback = f"No pude generar el comentario en este momento: {str(e)}"
            return EmotionResponse(obra_id=request.obra_id, comentario=fallback)

    def _build_prompt(self, estado_animo: str, painting) -> str:
        """
        Build prompt for Gemini API
        """
        return (
            f"Eres una IA que responde en español con un comentario breve, cálido y empático "
            f"(2-3 frases) para una persona que se siente '{estado_animo}'. "
            f"La obra seleccionada es '{painting.title}'. "
            f"Haz una reflexión artística amable y reconfortante relacionada con la obra."
        )
