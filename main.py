# main.py

from fastapi import FastAPI
from routers.routers import analyze
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(

    title="IA Agrícola - Análisis de Cultivos",
    description="Simulación de modelos de IA para análisis de imágenes de cultivos agrícolas.",
    version="1.0.0"
)

# 🚨 Agregá esto ANTES de incluir routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # podés usar ["*"] solo para pruebas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluir las rutas de análisis de imágenes
app.include_router(analyze, prefix="/api")
