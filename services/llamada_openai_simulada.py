import os
from dotenv import load_dotenv
from openai import OpenAI

# Carga las variables del archivo .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Inicializa el cliente de OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)


async def llamar_a_modelo_simulado(image_url: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Observa esta imagen de un cultivo y responde usando el siguiente formato, sin estilos de letras, solo en el formato, "
                            "si no es un cultivo natural solo pon en el nombre 'No es un cultivo', en el nombre no pongas otros comentarios, solo el nombre más certero:\n\n"
                            "nombre:\n"
                            "tipo_de_cultivo:\n"
                            "edad_aproximada:\n"
                            "tiempo_para_cosecha:\n"
                            "plagas_o_enfermedades:\n"
                            "recomendaciones:\n"
                            "clima_ideal:\n"
                            "temporada_recomendada:\n"
                            "tipo_de_suelo:\n"
                            "riego_recomendado:\n"
                            "fertilización:\n"
                            "indicadores_de_salud:\n"
                            "métodos_de_control:\n"
                            "cosecha_y_almacenamiento:\n"
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url}
                    }
                ]
            }
        ],
        max_tokens=1500
    )

    content = response.choices[0].message.content
    print("\n📤 Respuesta cruda del modelo:\n", content)

    return texto_a_json(content)



def texto_a_json(respuesta: str) -> dict:
    resultado = {}
    for linea in respuesta.strip().splitlines():
        if ':' in linea:
            clave, valor = linea.split(':', 1)
            resultado[clave.strip()] = valor.strip()
    return resultado
