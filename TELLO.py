import speech_recognition as sr
from djitellopy import Tello
import pyttsx3
import time
import os
from datetime import datetime
import cv2

# Inicializar pyttsx3
engine = pyttsx3.init()

def hablar(texto):
    print(texto)
    engine.say(texto)
    engine.runAndWait()

def escuchar_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        hablar("Escuchando comando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-ES").lower()
        hablar(f"Orden captada : {comando}")
        return comando
    except sr.UnknownValueError:
        hablar("No caché bien el comando, inténtalo otra vez.")
        return None
    except sr.RequestError as e:
        hablar(f"Servicio de reconocimiento fallido... El sistema se colapsa. ¿Intentamos otra vez o nos damos por vencidos? {e}")
        return None

def tomar_foto(dron):
    img = dron.get_frame_read().frame
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
    nombre_archivo = os.path.join(escritorio, f"foto_dron_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
    import cv2
    cv2.imwrite(nombre_archivo, img)
    hablar(f"Foto capturada y guardada en el escritorio bajo el nombre de {nombre_archivo}")

def grabar_video(dron, duracion_segundos=10):
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
    nombre_archivo = os.path.join(escritorio, f"video_dron_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi")
    hablar(f"Iniciando grabación de video por {duracion_segundos}  segundos... Que comience el espectáculo.")
    

    frame_read = dron.get_frame_read()
    
    # Obtener tamaño del frame
    frame = frame_read.frame
    height, width, _ = frame.shape
    
    # Configurar VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(nombre_archivo, fourcc, 20.0, (width, height))
    
    start_time = time.time()
    while time.time() - start_time < duracion_segundos:
        frame = frame_read.frame
        out.write(frame)
        time.sleep(0.05)  # pequeño delay para no saturar
    
    out.release()
    hablar(f"Grabación finalizada y guardada en el escritorio como un testimonio inmortal de tu genialidad. la nombre como {nombre_archivo}")

def main():
    dron = Tello()
    hablar("Conectando con “La que baja de las estrellas”... El cielo es nuestro reino, y esta estrella guía la misión. ¡Listos para despegar!")
    dron.connect()
    battery = dron.get_battery()
    hablar(f"Nivel de batería: {battery} por ciento")
    if battery < 20:
        hablar("Batería baja. Recarga el dron antes de volar, o prepárate para un aterrizaje forzoso.")
        return

    hablar("Despegando...")
    dron.takeoff()
    time.sleep(2)

    try:
        while True:
            comando = escuchar_comando()
            if comando is None:
                continue

            if "aterriza" in comando or "land" in comando:
                hablar("Aterrizando...")
                dron.land()
                break

            elif "izquierda" in comando or "mueve a la izquierda" in comando:
                hablar("Moviendo a la izquierda 50 centímetros")
                dron.move_left(50)

            elif "derecha" in comando or "mueve a la derecha" in comando:
                hablar("Moviendo a la derecha 50 centímetros")
                dron.move_right(50)

            elif "adelante" in comando or "mueve adelante" in comando:
                hablar("Moviendo hacia adelante 50 centímetros")
                dron.move_forward(50)

            elif "atrás" in comando or "mueve atrás" in comando:
                hablar("Moviendo hacia atrás 50 centímetros")
                dron.move_back(50)

            elif "gira a la izquierda" in comando or "gira izquierda" in comando:
                hablar("Rotando 90 grados a la izquierda")
                dron.rotate_counter_clockwise(90)

            elif "gira a la derecha" in comando or "gira derecha" in comando:
                hablar("Rotando 90 grados a la derecha")
                dron.rotate_clockwise(90)

            elif "sube" in comando or "subir" in comando:
                hablar("Subiendo 30 centímetros")
                dron.move_up(30)

            elif "baja" in comando or "bajar" in comando:
                hablar("Bajando 30 centímetros")
                dron.move_down(30)

            elif "foto" in comando or "tomar foto" in comando:
                tomar_foto(dron)

            elif "video" in comando or "grabar video" in comando:
                grabar_video(dron, duracion_segundos=10)

            elif "detente" in comando or "stop" in comando:
                hablar("Deteniendo movimiento")
                dron.send_rc_control(0, 0, 0, 0)

            else:
                hablar("Comando no reconocido, intenta otra vez.")

            time.sleep(1)

    except KeyboardInterrupt:
        hablar("Control finalizado por usuario. Misión cumplida, esperando nuevas órdenes, comandante.")

    finally:
        hablar("Aterrizando... Prepárate, que la estrella toca suelo con estilo y precisión.")
        dron.land()

if __name__ == "__main__":
    main()
