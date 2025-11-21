"""
Router for Gemini AI operations
"""
from fastapi import APIRouter, HTTPException, status
from api.app.services.gemini_service import GeminiService

router = APIRouter(prefix="/api/ia", tags=["ai"])


@router.get("/comentario")
async def generar_comentario(estado: str, obra: str):
    """
    Generate a comment using Gemini AI
    
    Args:
        estado: User's emotional state
        obra: Artwork description
        
    Returns:
        Generated comment
    """
    try:
        prompt = f"El usuario está {estado}. La obra es: {obra}. Responde con un comentario artístico simpático."
        gemini_service = GeminiService()
        comentario = await gemini_service.generar_comentario(prompt)
        return {"comentario": comentario}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error generating comment: {str(e)}"
        )

