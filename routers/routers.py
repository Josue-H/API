# routers/analyze.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.imgur_uploader import upload_image_to_imgur
# from services.modelo_cultivo_identificador import usar_modelo_entrenado_para_analizar_imagen
from services.llamada_openai_simulada import llamar_a_modelo_simulado

analyze = APIRouter()

# 👨‍🌾 Entrada esperada desde el frontend
class ImageInput(BaseModel):
    image_base64: str  # La imagen llega codificada en base64 desde el frontend

@analyze.post("/analyze-image")
async def analyze_image(payload: ImageInput):
    """
    Recibe una imagen en base64, la sube a Imgur, y la analiza usando un modelo simulado.
    """
    if not payload.image_base64.startswith("data:image"):
        raise HTTPException(status_code=400, detail="Imagen en base64 inválida")

    try:
        # 📤 Subimos la imagen a Imgur y obtenemos la URL pública
        img_url = await upload_image_to_imgur(payload.image_base64)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al subir imagen a Imgur: {e}")

    try:
        # 🧠 Ejecutamos la "simulación del modelo" (que usa GPT internamente)
        resultado = await llamar_a_modelo_simulado(img_url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el análisis del modelo: {e}")

    return {
        "image_url": img_url,
        "analisis": resultado
    }

