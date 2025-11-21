import google.generativeai as genai
from app.config import settings

class GeminiService:
    def __init__(self):
        genai.configure(api_key=settings.gemini_api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_comment(self, mood: str, painting_title: str) -> str:
        prompt = f"Generate a thoughtful comment about the painting '{painting_title}' based on the mood '{mood}'. Make it engaging and relevant."
        response = self.model.generate_content(prompt)
        return response.text