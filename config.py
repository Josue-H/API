# config.py
import os

# Clave de Imgur
IMGUR_CLIENT_ID = os.getenv("IMGUR_CLIENT_ID")

# Clave de API de OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ruta del modelo entrenado (.h5)
MODEL_PATH = os.getenv("MODEL_PATH")

# Ruta al archivo JSON con los nombres de las clases
CLASS_LABELS_PATH = os.getenv("CLASS_LABELS_PATH")

