"""
Service for interacting with Gemini API
"""
import httpx
from app.config import settings


class GeminiService:
    """Service for Gemini AI API integration"""
    
    def __init__(self):
        self.endpoint = settings.gemini_endpoint
        self.api_key = settings.gemini_api_key
    
    async def generar_comentario(self, prompt: str) -> str:
        """
        Generate a comment using Gemini API
        
        Args:
            prompt: The prompt to send to Gemini
            
        Returns:
            Generated comment text
        """
        # Escape quotes in prompt
        escaped_prompt = prompt.replace('"', "'")
        
        # Build request body according to Gemini API format
        json_body = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": escaped_prompt
                        }
                    ]
                }
            ]
        }
        
        url = f"{self.endpoint}?key={self.api_key}"
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                response = await client.post(
                    url,
                    json=json_body,
                    headers={"Content-Type": "application/json"}
                )
                response.raise_for_status()
                
                body = response.json()
                return self._extraer_texto(body)
            except httpx.HTTPError as e:
                raise Exception(f"Error calling Gemini API: {str(e)}")
    
    def _extraer_texto(self, json_response: dict) -> str:
        """
        Extract text from Gemini API response
        
        Args:
            json_response: JSON response from Gemini API
            
        Returns:
            Extracted text
        """
        try:
            candidates = json_response.get("candidates", [])
            if candidates and len(candidates) > 0:
                content = candidates[0].get("content", {})
                parts = content.get("parts", [])
                if parts and len(parts) > 0:
                    return parts[0].get("text", "")
            return "No se pudo extraer el texto de la respuesta"
        except Exception as e:
            return f"Error al procesar respuesta: {str(e)}"

