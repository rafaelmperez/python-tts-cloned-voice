# Python TTS — Cloned AI Voice (ElevenLabs & OpenAI TTS)

Turn any text into speech using your cloned AI voice — powered by **Python**, **ElevenLabs**, and **OpenAI TTS**.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🧠 Overview
Este proyecto proporciona un **script CLI en Python** (`tts_script.py`) que convierte texto en audio usando tu **voz clonada** (vía **ElevenLabs**) o una **voz neural realista** (vía **OpenAI TTS**). Está pensado para:
- Desarrolladores que quieren **TTS profesional** en flujos de trabajo/automatizaciones.
- Demostraciones técnicas, prototipos y contenido multimedia.
- Un código **limpio, extensible y documentado**, listo para producción ligera.

## 🚀 Features
- ✅ Entrada por **argumento CLI**, **archivo .txt** o **prompt interactivo**.
- ✅ Soporte real para **ElevenLabs** (voz clonada) y **OpenAI TTS**.
- ✅ Configuración con **`.env`** (API keys, VOICE_ID, proveedor).
- ✅ **Logging** en consola y archivo (`tts_log.txt`).
- ✅ Manejo de **errores** y salidas en **MP3/WAV**.
- ✅ Arquitectura **extensible** para nuevos proveedores.

## 🧩 Tech Stack
- **Python 3.10+**
- **ElevenLabs API**, **OpenAI TTS**
- `requests`, `python-dotenv`, `openai`
- CLI con `argparse`, logs con `logging`

## ⚙️ Installation

```bash
# 1) Clonar el repositorio
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>

# 2) Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate

# 3) Instalar dependencias
pip install -r requirements.txt

# 4) Crear carpeta de salida (si no existe)
mkdir -p audio_outputs
