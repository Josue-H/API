import os
import httpx
import base64
from urllib.parse import urlencode
import requests

UPLOADCARE_PUBLIC_KEY = "34d20300d53b98b547bb"



async def upload_image_to_imgur(base64_str: str) -> str:
    if "," not in base64_str or not base64_str.startswith("data:image"):
        raise ValueError("⚠️ Formato base64 inválido. Falta encabezado tipo data:image/...")

    header, b64_data = base64_str.split(",", 1)
    mime_type = header.split(";")[0].split(":")[1]

    image_bytes = base64.b64decode(b64_data)

    files = {
        'file': ('image.jpg', image_bytes, mime_type)
    }

    data = {
        'UPLOADCARE_PUB_KEY': UPLOADCARE_PUBLIC_KEY,
        'UPLOADCARE_STORE': '1'
    }

    async with httpx.AsyncClient() as client:
        response = await client.post('https://upload.uploadcare.com/base/', data=data, files=files)

    if response.status_code != 200:
        raise Exception(f"Error al subir imagen a Uploadcare: {response.status_code} {response.text}")

    file_id = response.json().get("file")
    if not file_id:
        raise Exception("❌ No se encontró el campo 'file' en la respuesta.")

    return f"https://ucarecdn.com/{file_id}/"