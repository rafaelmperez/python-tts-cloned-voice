#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TTS Script - Conversión de texto a voz con tu voz clonada
Compatible con ElevenLabs y OpenAI TTS
Autor: TuNombre
Versión: 1.2
"""

import os
import sys
import argparse
import logging
from dotenv import load_dotenv
import requests
import openai

# -----------------------------
# CONFIGURACIÓN DE LOGGING
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("tts_log.txt"),
        logging.StreamHandler()
    ]
)

# -----------------------------
# CARGAR VARIABLES DE ENTORNO
# -----------------------------
load_dotenv()

API_KEY = os.getenv("API_KEY")
VOICE_ID = os.getenv("VOICE_ID")
TTS_PROVIDER = os.getenv("TTS_PROVIDER", "elevenlabs").lower()

OUTPUT_DIR = "audio_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# FUNCIONES AUXILIARES
# -----------------------------
def read_text_input(file_path: str = None, input_text: str = None) -> str:
    """Lee texto desde un archivo o desde el argumento del usuario."""
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except Exception as e:
            logging.error(f"Error al leer el archivo: {e}")
            sys.exit(1)
    elif input_text:
        return input_text.strip()
    else:
        return input("Introduce el texto que deseas convertir a voz:\n> ").strip()


def save_audio(content: bytes, filename: str = "output.mp3") -> str:
    """Guarda los bytes de audio en un archivo."""
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "wb") as f:
        f.write(content)
    logging.info(f"✅ Audio guardado en: {path}")
    return path

# -----------------------------
# FUNCIONES DE CADA PROVEEDOR
# -----------------------------
def tts_elevenlabs(text: str) -> str:
    """Genera audio usando la API de ElevenLabs."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.7, "similarity_boost": 0.9}
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return save_audio(response.content, "output_elevenlabs.mp3")
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error en ElevenLabs API: {e}")
        sys.exit(1)


def tts_openai(text: str) -> str:
    """Genera audio usando OpenAI TTS (modelo gpt-4o-mini-tts)."""
    openai.api_key = API_KEY
    try:
        logging.info("Enviando texto a OpenAI TTS...")
        response = openai.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",  # Se puede cambiar a "verse", "aria", etc.
            input=text
        )
        audio_bytes = response.read()
        return save_audio(audio_bytes, "output_openai.mp3")
    except Exception as e:
        logging.error(f"❌ Error en OpenAI TTS: {e}")
        sys.exit(1)


# -----------------------------
# SELECCIÓN DE PROVEEDOR
# -----------------------------
def generate_tts_audio(text: str) -> str:
    """Selecciona el proveedor TTS según la variable de entorno."""
    if TTS_PROVIDER == "elevenlabs":
        return tts_elevenlabs(text)
    elif TTS_PROVIDER == "openai":
        return tts_openai(text)
    else:
        logging.error(f"Proveedor TTS '{TTS_PROVIDER}' no soportado.")
        sys.exit(1)


# -----------------------------
# FUNCIÓN PRINCIPAL
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Convertir texto a voz con tu voz clonada.")
    parser.add_argument("text", nargs="?", help="Texto a convertir en audio.")
    parser.add_argument("-f", "--file", help="Ruta a un archivo .txt con el texto.")
    args = parser.parse_args()

    text = read_text_input(args.file, args.text)
    if not text:
        logging.error("❌ No se proporcionó texto válido.")
        sys.exit(1)

    logging.info(f"🔊 Generando audio usando: {TTS_PROVIDER.upper()}")
    generate_tts_audio(text)


if __name__ == "__main__":
    main()


"""
==============================
README
==============================

📦 CONFIGURACIÓN:
1. Crea un archivo `.env` en este directorio con el siguiente contenido:

    API_KEY=tu_api_key_aqui
    VOICE_ID=tu_voice_id_aqui
    TTS_PROVIDER=elevenlabs

   🔹 Usa `TTS_PROVIDER=openai` para usar el motor de OpenAI.
   🔹 Usa `TTS_PROVIDER=elevenlabs` para usar tu voz clonada en ElevenLabs.

2. Instala las dependencias:
    pip install -r requirements.txt

3. Crea la carpeta de salida si no existe:
    mkdir audio_outputs

🚀 EJEMPLOS DE USO:

- Texto directo:
    python tts_script.py "Hola, esta es mi voz clonada."

- Desde archivo:
    python tts_script.py -f texto.txt

📚 CAMBIAR DE MOTOR:
Edita `.env` y cambia:
    TTS_PROVIDER=openai  o  TTS_PROVIDER=elevenlabs

🧩 NOTAS:
- ElevenLabs requiere `VOICE_ID` y una voz clonada previamente.
- OpenAI genera una voz realista (no clonada) con `gpt-4o-mini-tts`.
- Los archivos se guardan automáticamente en `audio_outputs/`.
"""

