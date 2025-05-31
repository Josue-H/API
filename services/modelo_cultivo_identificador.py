# # services/modelo_cultivo_identificador.py

# import numpy as np
# import requests
# import time
# import json
# from io import BytesIO
# from PIL import Image
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
# from tensorflow.nn import softmax
# from config import MODEL_PATH, CLASS_LABELS_PATH
# from services.llamada_openai_simulada import llamar_a_modelo_simulado

# async def usar_modelo_entrenado_para_analizar_imagen(image_url: str) -> dict:


#     try:
#         start_time = time.time()

#         # 📥 Cargar etiquetas de clases
#         with open(CLASS_LABELS_PATH) as f:
#             class_indices = json.load(f)
#         idx_to_class = {v: k for k, v in class_indices.items()}

#         # 🧠 Cargar modelo entrenado
#         print("📦 Cargando modelo...")
#         model = load_model(MODEL_PATH)

#         # 🌐 Descargar y procesar imagen
#         print("🧼 Procesando imagen...")
#         response = requests.get(image_url)
#         response.raise_for_status()
#         image = Image.open(BytesIO(response.content)).convert("RGB")
#         image = image.resize((224, 224))
#         image_array = img_to_array(image)
#         image_array = preprocess_input(image_array)
#         image_array = np.expand_dims(image_array, axis=0)

#         # 🔍 Inferencia
#         print("🤖 Ejecutando predicción...")
#         predictions = model.predict(image_array)
#         probabilities = softmax(predictions[0]).numpy()

#         top_k = 3
#         top_indices = np.argsort(probabilities)[::-1][:top_k]
#         top_classes = [
#             {
#                 "clase": idx_to_class[i],
#                 "probabilidad": float(np.round(probabilities[i], 4))
#             } for i in top_indices
#         ]

#         predicted_label = top_classes[0]["clase"]
#         confidence = top_classes[0]["probabilidad"]

#         resultado_real = {
#             "modelo": "modelo_cultivos.h5",
#             "prediccion_principal": predicted_label,
#             "confianza": confidence,
#             "top_3": top_classes,
#             "tiempo_procesamiento": f"{round(time.time() - start_time, 2)}s",
#             "origen": "modelo_real"
#         }

#         print(f"✅ Resultado del modelo real: {resultado_real}")

#     except Exception as e:
#         print(f"❌ Error al usar el modelo real: {e}")
#         resultado_real = {
#             "error": "No se pudo ejecutar el modelo real",
#             "detalle": str(e)
#         }

#     # 🪄 GPT hace la magia real, pero se disfraza de modelo
#     resultado_simulado = await llamar_a_modelo_simulado(image_url)

#     return {
#         "modelo": "modelo_cultivos_simulado_v1",
#         "resultado": resultado_simulado,
#         "origen": "modelo_simulado_usando_GPT",
#         "referencia_real": resultado_real  # opcional, puedes omitirlo si no quieres mostrarlo
#     }
