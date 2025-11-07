# 🗣️ Python TTS — Cloned AI Voice (ElevenLabs & OpenAI TTS)

Turn any text into speech using your cloned AI voice — powered by **Python**, **ElevenLabs**, and **OpenAI TTS**.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🧠 Overview

Este proyecto proporciona un **script CLI en Python** (`tts_script.py`) que convierte texto en audio usando tu **voz clonada** (vía **ElevenLabs**) o una **voz neural realista** (vía **OpenAI TTS**).  

Está pensado para:
- Desarrolladores que quieren **TTS profesional** en flujos de trabajo o automatizaciones.
- Demostraciones técnicas, prototipos y contenido multimedia.
- Un código **limpio, extensible y documentado**, listo para producción ligera.

---

## 🚀 Features

- ✅ Entrada por **argumento CLI**, **archivo .txt** o **prompt interactivo**.  
- ✅ Soporte real para **ElevenLabs (voz clonada)** y **OpenAI TTS (voz neural)**.  
- ✅ Configuración con **`.env`** (API keys, VOICE_ID, proveedor).  
- ✅ **Logging** en consola y archivo (`tts_log.txt`).  
- ✅ Manejo de **errores** y salidas en **MP3/WAV**.  
- ✅ Arquitectura **extensible** para nuevos proveedores.

---

## 🧩 Tech Stack

- **Python 3.10+**
- **ElevenLabs API**, **OpenAI TTS**
- Librerías: `requests`, `python-dotenv`, `openai`
- CLI con `argparse`
- Sistema de logs con `logging`

---

## ⚙️ Installation

```bash
# 1️⃣ Clonar el repositorio
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>

# 2️⃣ Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3️⃣ Instalar dependencias
pip install -r requirements.txt

# 4️⃣ Crear carpeta de salida (si no existe)
mkdir -p audio_outputs
````

---

## 🔐 Configuration (.env)

Crea un archivo llamado `.env` en la raíz del proyecto con tus credenciales API.

### 🗣️ ElevenLabs (voz clonada)

```dotenv
API_KEY=tu_api_key_de_elevenlabs
VOICE_ID=tu_voice_id_clonada
TTS_PROVIDER=elevenlabs
```

### 🧠 OpenAI TTS (voz neural)

```dotenv
API_KEY=tu_api_key_de_openai
TTS_PROVIDER=openai
```

| Variable       | Descripción                                 | Obligatoria |
| -------------- | ------------------------------------------- | ----------- |
| `API_KEY`      | Clave de API del proveedor seleccionado     | ✅           |
| `VOICE_ID`     | ID de la voz clonada (solo para ElevenLabs) | ✅ (EL)      |
| `TTS_PROVIDER` | Proveedor usado (`elevenlabs` o `openai`)   | ✅           |

> ⚠️ **Importante:** No subas el archivo `.env` a GitHub. Contiene datos sensibles.

---

## 🎙️ Usage

### 🔹 Texto directo:

```bash
python tts_script.py "Hola, esta es mi voz clonada"
```

### 🔹 Desde archivo `.txt`:

```bash
python tts_script.py -f texto.txt
```

### 🔹 Modo interactivo:

```bash
python tts_script.py
```

🎧 Los audios generados se guardan en:

```
audio_outputs/output_elevenlabs.mp3
```

o

```
audio_outputs/output_openai.mp3
```

---

## 🧰 Supported Providers

| Proveedor      | Ventajas principales                           | Requisitos                                       |
| -------------- | ---------------------------------------------- | ------------------------------------------------ |
| **ElevenLabs** | Clonado de voz con realismo profesional        | `API_KEY`, `VOICE_ID`, `TTS_PROVIDER=elevenlabs` |
| **OpenAI TTS** | Voces neurales de alta calidad y baja latencia | `API_KEY`, `TTS_PROVIDER=openai`                 |

---

## 🪄 Extensibility

El script está diseñado para ampliarse fácilmente:

1. Crea una nueva función `tts_<proveedor>()`.
2. Añade tu API o SDK correspondiente.
3. Registra el nuevo proveedor en `generate_tts_audio()`.
4. Añade tus variables al `.env`.

Ejemplos de posibles integraciones:

* Play.ht
* OpenVoice
* VITS / Tacotron2 (local)

---

## 🧠 Error Handling

* **401 Unauthorized:** API key o VOICE_ID incorrectos.
* **Red/Timeout:** errores de conexión manejados con `try/except`.
* **Archivo inválido:** se notifica por consola y se aborta la ejecución.
* **Sin texto:** se valida antes de llamar a la API.

---

## 🧾 Logging

El sistema de logs registra:

* Proveedor usado
* Errores y respuestas
* Ruta de salida

Archivo de registro: `tts_log.txt`

Formato de ejemplo:

```
2025-11-07 14:22:10 [INFO] 🔊 Generando audio usando: ELEVENLABS
2025-11-07 14:22:11 [INFO] ✅ Audio guardado en: audio_outputs/output_elevenlabs_3.mp3
```

---

## 🧩 Project Structure

```
python-tts-cloned-voice/
├─ tts_script.py
├─ requirements.txt
├─ .gitignore
├─ LICENSE
├─ README.md
├─ audio_outputs/
└─ tts_log.txt
```

---

## 💡 Contributing

Contribuciones son bienvenidas 💬

1. Crea una rama `feature/<nombre>` o `fix/<nombre>`.
2. Cumple con las normas **PEP8** y añade **docstrings**.
3. Prueba los cambios antes de enviar un Pull Request.

---

## 📜 License

Distribuido bajo la licencia **MIT**.
Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 💬 Acknowledgements

* [ElevenLabs](https://elevenlabs.io) — por su API de clonación de voz.
* [OpenAI](https://platform.openai.com/) — por su TTS neural.
* Comunidad open-source de Python.

---

## 🔎 GitHub SEO

**Keywords:**
`python`, `text-to-speech`, `tts`, `ai`, `voice-cloning`, `openai`, `elevenlabs`, `automation`, `audio`, `speech-synthesis`

**One-liner SEO description:**

> Convert any text into natural-sounding speech using your cloned AI voice — built with Python, ElevenLabs, and OpenAI TTS.

---

**GitHub Topics:**
`python` · `text-to-speech` · `tts` · `ai` · `voice-cloning` · `openai` · `elevenlabs` · `automation` · `audio` · `speech-synthesis`

