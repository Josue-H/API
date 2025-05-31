import base64
import httpx
# from config import IMGUR_CLIENT_ID

async def upload_image_to_imgur(base64_str: str) -> str:
    if "," not in base64_str:
        raise ValueError("Formato base64 inválido. Falta encabezado.")

    b64_data = base64_str.split(",")[1]
    image_bytes = base64.b64decode(b64_data)

    headers = {"Authorization": "Client-ID 2651b0967ee70c4"}


    # 🔁 Usamos files, igual que en requests
    files = {"image": ("image.jpg", image_bytes, "image/jpeg")}

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.imgur.com/3/image", headers=headers, files=files)

    if response.status_code != 200:
        print("🛑 Imgur error:", response.status_code, response.text)
        raise Exception("Error al subir imagen a Imgur")

    return response.json()["data"]["link"]
