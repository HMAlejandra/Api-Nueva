import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generar_comentario(emocion, obra):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Genera un comentario breve y expresivo sobre la obra de arte '{obra}' que transmita la emoción '{emocion}'. El comentario debe ser en español."
    response = model.generate_content(prompt)
    return response.text