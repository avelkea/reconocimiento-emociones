import cv2
import mediapipe as mp
import numpy as np
from deepface import DeepFace

# Inicializar MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir imagen a RGB (DeepFace y MediaPipe requieren RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar la imagen con FaceMesh
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            height, width, _ = frame.shape
            
            # Obtener coordenadas de puntos clave específicos
            landmarks = np.array([(int(l.x * width), int(l.y * height)) for l in face_landmarks.landmark])

            # Dibujar los puntos en la cara
            for x, y in landmarks:
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

    # Usar DeepFace para analizar la emoción
    try:
        analysis = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
        emotion = analysis[0]['dominant_emotion']
    except:
        emotion = "No Detectado"

    # Mostrar la emoción detectada
    cv2.putText(frame, f"Emocion: {emotion}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)

    # Mostrar la imagen con detección de emociones
    cv2.imshow("FaceMesh Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()