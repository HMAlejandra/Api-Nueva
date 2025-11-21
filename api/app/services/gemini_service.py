"""
Service for interacting with Gemini API
"""
import google.generativeai as genai
from api.app.config.settings import settings


class GeminiService:
    """Service for Gemini AI API integration"""

    def __init__(self):
        self.api_key = settings.gemini_api_key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    async def generar_comentario(self, prompt: str) -> str:
        """
        Generate a comment using Gemini API (async)
        """
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Error calling Gemini API: {str(e)}")
