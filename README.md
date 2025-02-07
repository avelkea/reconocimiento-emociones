# Reconocimiento de emociones con OpenCV y Mediapipe
Mediante el uso de OpenCV, Mediapipe, Deepface y Python se clasifican emociones en tiempo real.

## 📑 Tabla de Contenido
1. [Ejemplo de ejecución del programa usando OpenCV y Mediapipe](#ejemplo-de-ejecucion-del-programa-usando-opencv-y-mediapipe)
2. [Ejemplo de ejecución del programa usando OpenCV, Mediapipe y DeepFace](#ejemplo-de-ejecucion-del-programa-usando-opencv-mediapipe-y-deepface)
3. [Tecnologías utilizadas](#tecnologías)
4. [Funcionamiento](#funcionamiento)
5. [Características](#caracteristicas)
6. [Instalación y Configuración](#instalacion-y-configuracion)  
   - [Crear y activar el entorno virtual](#crear-y-activar-el-entorno-virtual)  
   - [Instalar requirements](#instalar-requirements)
7. [Links a los códigos](#links-a-los-codigos)

---

## Ejemplo de ejecución del programa usando Open Cv y Mediapipe <a name="#ejemplo-de-ejecucion-del-programa-usando-opencv-y-mediapipe"></a>
![Ejemplo de Detección](imagenes/imagen1.png)
## Ejemplo de ejecución del programa usando Open Cv, Mediapipe y Deepface <a name="ejemplo-de-ejecucion-del-programa-usando-opencv-mediapipe-y-deepface"></a>
![Ejemplo de Detección](imagenes/imagen2.png)

## Tecnologías utilizadas <a name="tecnologías"></a>
-**Deep Face:** Para el reconocimiento de emociones
-**MediaPipe:** Para la detección de rostros en tiempo real
-**OpenCV:** Para la manipulación de imágenes y video


## Funcionamiento <a name="funcionamiento"></a>


## Características <a name="caracteristicas"></a>
- Detecta hasta 2 rostros usando MediaPipe
- Detecta y visualiza puntos clave en la cara y los dibuja con puntos color verde
- El modelo indentifica emciones como : neutral, sorprendido, enojado.
- Se muestra la emoción detectada

## Instalación y configuración <a name="instalacion-y-configuracion"></a>
```bash
git clone https://github.com/usuario/proyecto-emociones.git
cd proyecto-emociones
```

### Crear y activar el entorno virtual <a name="#crear-y-activar-el-entorno-virtual"></a>
```bash
python -m venv env
source env/bin/activate  # En macOS/Linux
env\Scripts\activate     # En Windows
```
### Instalar requirements <a name="#instalar-requirements"></a>
```bash
pip install -r requirements.txt
```
## Links a los códigos <a name="#links-a-los-codigos"></a>
[Código usando Mediapipe](src/prueba2.py)

[Código usando Deepface](src/prueba3.py)
