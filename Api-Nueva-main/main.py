from fastapi import FastAPI, Query
from pydantic import BaseModel
from ai import generar_comentario

app = FastAPI(
    title="API IA Terapia de Arte – Gemini",
    version="1.0"
)

# ======================
#  GET → /api/ia/comentario
# ======================
@app.get("/api/ia/comentario")
def comentario(
    estado: str = Query(..., description="Estado emocional del usuario"),
    obra: str = Query(..., description="Nombre o descripción de la obra")
):
    resultado = generar_comentario(estado, obra)
    return {"comentario": resultado}


# ======================
#  POST → /api/ia/emotions
# ======================
class EmotionRequest(BaseModel):
    estado_animo: str
    obra_id: int


class EmotionResponse(BaseModel):
    comentario: str


@app.post("/api/ia/emotions", response_model=EmotionResponse)
def post_emotion(req: EmotionRequest):
    # Aquí normalmente consultarías la obra en la BD:
    # obra = db.query(Obras).filter_by(id=req.obra_id).first()
    # nombre_obra = obra.nombre
    #
    # Para ejemplo directo:
    nombre_obra = f"Obra #{req.obra_id}"

    resultado = generar_comentario(req.estado_animo, nombre_obra)
    return EmotionResponse(comentario=resultado)
