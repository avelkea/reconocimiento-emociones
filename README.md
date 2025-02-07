# Reconocimiento de emociones con OpenCV y Mediapipe
Mediante el uso de OpenCV, Mediapipe, Deepface y Python se clasifican emociones en tiempo real.

## Ejemplo de ejecución del programa usando Open Cv y Mediapipe
![Ejemplo de Detección](imagenes/imagen1.png)
## Ejemplo de ejecución del programa usando Open Cv, Mediapipe y Deepface
![Ejemplo de Detección](imagenes/imagen2.png)

## Características
- Detecta hasta 2 rostros usando MediaPipe
- Detecta y visualiza puntos clave en la cara y los dibuja con puntos color verde
- El modelo indentifica emciones como : neutral, sorprendido, enojado.
- Se muestra la emoción detectada

## Instalación y configuración 
```bash
git clone https://github.com/usuario/proyecto-emociones.git
cd proyecto-emociones
```

### Crear y activar el entorno virtual
```bash
python -m venv env
source env/bin/activate  # En macOS/Linux
env\Scripts\activate     # En Windows
```
### Instalar requirements
```bash
pip install -r requirements.txt
