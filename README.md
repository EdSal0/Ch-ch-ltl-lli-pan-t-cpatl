
# Control de Dron Tello por Voz en Español

Este proyecto permite controlar un dron **DJI Tello** usando comandos de voz en español, con retroalimentación hablada y funciones para tomar fotos y grabar videos directamente desde el dron.

---

## Características

- Control por voz para movimientos básicos: avanzar, retroceder, girar, subir, bajar, moverse a izquierda y derecha.
- Comandos para tomar fotos y grabar videos con duración configurable.
- Feedback hablado con síntesis de voz (`pyttsx3`) para confirmar acciones.
- Reconocimiento de voz en español usando Google Speech Recognition.
- Guarda fotos y videos automáticamente en el escritorio del usuario con timestamp.
- Detección de nivel de batería antes del vuelo para seguridad.

---

## Requisitos

- Python 3.x
- Biblioteca `djitellopy` para controlar el dron Tello.
- Biblioteca `speech_recognition` para reconocimiento de voz.
- Biblioteca `pyttsx3` para síntesis de voz.
- Biblioteca `opencv-python` (cv2) para manejo de video y captura de imágenes.
- Micrófono conectado y configurado.
- Dron DJI Tello conectado a la red Wi-Fi.

---
¡Listo para volar con voz y estilo! 🚁🎤-
## Instalación

1. Clonar este repositorio o copiar el script.
2. Instalar dependencias con pip:

```bash
pip install djitellopy speechrecognition pyttsx3 opencv-python


