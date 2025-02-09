# Reconocimiento de emociones con OpenCV y Mediapipe
Mediante el uso de OpenCV, Mediapipe, Deepface y Python se clasifican emociones en tiempo real.

##  Tabla de Contenido
1. [Ejemplo de ejecución del programa usando OpenCV y Mediapipe](#ejemplo-de-ejecucion-del-programa-usando-opencv-y-mediapipe)
2. [Ejemplo de ejecución del programa usando OpenCV, Mediapipe y DeepFace](#ejemplo-de-ejecucion-del-programa-usando-opencv-mediapipe-y-deepface)
3. [Tecnologías utilizadas](#tecnologías)
4. [Funcionamiento](#funcionamiento)
5. [Características](#caracteristicas)
6. [Instalación y Configuración](#instalacion-y-configuracion)  
   - [Crear y activar el entorno virtual](#crear-y-activar-el-entorno-virtual)  
   - [Instalar requirements](#instalar-requirements)
7. [Links a los códigos](#links-a-los-codigos)
8. [Problemas presentadfos a lo largo del proyecto](#problemas)

---

## Ejemplo de ejecución del programa usando Open Cv y Mediapipe <a name="#ejemplo-de-ejecucion-del-programa-usando-opencv-y-mediapipe"></a>
![Ejemplo de Detección](imagenes/imagen1.png)
## Ejemplo de ejecución del programa usando Open Cv, Mediapipe y Deepface <a name="ejemplo-de-ejecucion-del-programa-usando-opencv-mediapipe-y-deepface"></a>
![Ejemplo de Detección](imagenes/imagen2.png)

## Tecnologías utilizadas <a name="tecnologías"></a>

+ **Deep Face:** Para el reconocimiento de emociones

+ **MediaPipe:** Para la detección de rostros en tiempo real

+ **OpenCV:** Para la manipulación de imágenes y video


## Funcionamiento <a name="funcionamiento"></a>
```python
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=2,  # Máximo de 2 caras
)
```
Aquí se inicializa un objeto que accede a FaceMesh, un módulo dentro de MediaPipe, este se configura para que se puedan detectar dos rostros al mismo tiempo. Prepara el modelo para cuando se quiera llamar para procesar las mallas de las caras.
```python
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
```
Se accede a la primera cámara disponible dentro del sistema (0). En ret se establece si hay un flujo de frames desde la camara, en frame se obtiene una matriz tridimensional que contiene el ancho y alto de los pixeles y los canales de las imagenes. Los canales son 3 (BGR), estos tienen un valor de 0 a 255 que indican la intensidad de azul, verde y rojo dentro de cada pixel. EL video es una sucesión muy rápida de imágenes capturadas que se muestran en la pantalla de manera continua. 
```python
results = face_mesh.process(rgb_frame)
```
MediaPipe ejecuta la detección de landmarks facieles en la imagen con ayuda de una red neuronal que identifica 468 puntos clave que en lugares como ojos, cejas, nariz, boca, etc. Después, se calculan las posiciones relativas de los landmarks faciales de la persona y devuelve unas coordenadas que sirven para dibujar los puntos.
```python
mouth_opening = np.linalg.norm(landmarks[MOUTH[0]] - landmarks[MOUTH[1]])
            eyebrow_distance = np.linalg.norm(landmarks[LEFT_EYEBROW[0]] - landmarks[LEFT_EYEBROW[2]])
```
Se utilizan dos índices de los puntos clave de las cejas y la boca para ver la separacion de estos. Con la fórmula de distancia entre dos puntos se establece la distancia de separación. 
d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

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

## Problemas presentados durante el desarrollo del proyecto <a name="#problemas"></a>
1. **OpenCv no detectaba la cámara:**
    +	**Problema**: OpenCV arrojaba el error:
      
       can't open camera by index
   >
    lo que indicaba que no podía acceder a /dev/video0.
    +	**Causa**: Pi Camera Module 3 no usa V4L2 (Video4Linux2) por defecto, sino que está diseñada para funcionar con libcamera en Raspberry Pi OS.
    +	**Solución**: Se intentó con `v4l2-ctl --list-devices`
     	 para identificar los dispositivos y usando `libcamera-hello`, que sí reconoció la cámara.

2. **Se detectaban muchos dispositivos en /dev/video:**
   + **Problema:** ls /dev/video* arrojaba una gran cantidad de dispositivos (/dev/video0, /dev/video1, /dev/video20-/dev/video35), lo que hacía difícil identificar cuál era la cámara real.
	+ **Causa:** Raspberry Pi usa varios dispositivos virtuales para la GPU, procesamiento de video y diferentes pipelines de captura.
	+	**Solución:** Se ejecutó `v4l2-ctl --list-devices` y `libcamera-hello --list-cameras` para identificar la cámara correcta, que resultó ser imx708 con /dev/video0.

3. **Problemas al instalar picamera2:**
	+	**Problema:** Se intentó instalar picamera2, pero arrojaba el error:
   > No module named 'libcamera'

  	
También falló la instalación de pykms, una dependencia requerida para la visualización con DRM.
   +  **Causa:**
	    1.	libcamera no estaba disponible en el entorno virtual.
	    2.	Se intentó instalar pykms, pero no existe en PyPI y no se podía instalar con pip.
   + **Solución:**
	    1. Se enlazó libcamera dentro del entorno virtual, pero al final no funcionó correctamente con picamera2.
	    2. Se recomendó usar libcamera directamente en lugar de OpenCV/V4L2.
    
 4. **No aparecía la imagen en la transmisión de Flask:**
	+ **Problema:** Aunque Flask estaba corriendo en la Raspberry Pi, al acceder desde otra computadora en http://192.168.100.17:5000/video_feed, la página aparecía en blanco.
	+ **Causa:**
 	    1. OpenCV no estaba accediendo correctamente a la cámara.
	    2. La IP era accesible, pero Chrome bloqueaba la conexión (probablemente por HTTP en lugar de HTTPS).
	+ **Solución:**
	    1. Se probó abrir http://192.168.100.17:5000 en Safari, y funcionó, lo que confirmó que Chrome estaba bloqueando la conexión.

