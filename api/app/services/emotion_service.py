"""
Service for emotion-based artwork recommendations
"""
from typing import Optional
from sqlalchemy.orm import Session
from api.app.schemas.emotion import EmotionRequest, EmotionResponse
from api.app.repositories.artwork_repository import ArtworkRepository
from api.app.services.gemini_service import GeminiService
from api.app.config import settings


class EmotionService:
    """Service for generating emotion-based comments"""
    
    def __init__(self, db: Session):
        self.artwork_repository = ArtworkRepository(db)
        self.gemini_service = GeminiService()
    
    async def generar_comentario(self, request: EmotionRequest) -> EmotionResponse:
        """
        Generate a comment based on user's emotional state and artwork
        
        Args:
            request: Emotion request with estado_animo and obra_id
            
        Returns:
            Emotion response with comentario
        """
        # Get artwork from database
        artwork = self.artwork_repository.find_by_id(request.obra_id)
        
        if not artwork:
            # Fallback for unknown artwork
            fallback = (
                f"Sobre tu estado '{request.estado_animo}' y la obra desconocida: "
                "respira, observa los detalles y recuerda que el arte puede acompañarte."
            )
            return EmotionResponse(obra_id=request.obra_id, comentario=fallback)
        
        # Build prompt
        prompt = self._build_prompt(request.estado_animo, artwork)
        
        # Check if Gemini API is configured
        endpoint = settings.gemini_endpoint
        api_key = settings.gemini_api_key
        
        if not endpoint or not api_key:
            # Fallback response
            fallback = (
                f"Sobre tu estado '{request.estado_animo}' y la obra '{artwork.title}' "
                f"de {artwork.author}: respira, observa los detalles y recuerda que el arte puede acompañarte."
            )
            return EmotionResponse(obra_id=request.obra_id, comentario=fallback)
        
        try:
            # Call Gemini service
            comentario = await self.gemini_service.generar_comentario(prompt)
            return EmotionResponse(obra_id=request.obra_id, comentario=comentario)
        except Exception as e:
            # Fallback on error
            fallback = f"Ocurrió un error al generar el comentario: {str(e)}"
            return EmotionResponse(obra_id=request.obra_id, comentario=fallback)
    
    def _build_prompt(self, estado_animo: str, artwork) -> str:
        """
        Build prompt for Gemini API
        
        Args:
            estado_animo: User's emotional state
            artwork: Artwork object
            
        Returns:
            Formatted prompt string
        """
        return (
            f"Eres una IA que responde en español con un comentario breve y empático (2-3 frases) "
            f"para alguien que se siente '{estado_animo}'. "
            f"La obra es '{artwork.title}' de {artwork.author}. "
            f"Descripción: {artwork.description or 'Sin descripción'}. "
            f"Haz un comentario amistoso, creativo y reconfortante, referencia breve a la obra."
        )

