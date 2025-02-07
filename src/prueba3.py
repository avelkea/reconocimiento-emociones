import cv2
import mediapipe as mp
import numpy as np
from deepface import DeepFace

# Inicializar MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=2,  # Soporte para 2 caras
)

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

    face_positions = []  # Almacenar coordenadas de cada cara detectada

    if results.multi_face_landmarks:
        height, width, _ = frame.shape

        for face_landmarks in results.multi_face_landmarks:
            # Obtener coordenadas de landmarks faciales
            landmarks = np.array([(int(l.x * width), int(l.y * height)) for l in face_landmarks.landmark])

            # Dibujar los puntos en la cara
            for x, y in landmarks:
                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

            # Determinar la posición central de la cara
            face_x = int(np.mean(landmarks[:, 0]))  # Centro X de la cara
            face_y = int(np.mean(landmarks[:, 1]))  # Centro Y de la cara

            face_positions.append((face_x, face_y))  # Guardar la posición de cada cara

    # Usar DeepFace para analizar emociones
    try:
        analysis = DeepFace.analyze(rgb_frame, actions=['emotion'], enforce_detection=False)
        
        for i, face in enumerate(analysis):
            if i < len(face_positions):  # Asegurar que hay coordenadas para cada cara detectada
                emotion = face['dominant_emotion']
                x, y = face_positions[i]

                # Ajustar la posición del texto cerca de la cara detectada
                text_x = x - 50  # Mueve el texto a la izquierda de la cara
                text_y = y - 50  # Mueve el texto hacia arriba
                
                # Mostrar la emoción detectada cerca de la cara correspondiente
                cv2.putText(frame, f"Emocion: {emotion}", (text_x, text_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    except:
        pass  # Si no se detectan emociones, simplemente ignorar

    # Mostrar la imagen con detección de emociones
    cv2.imshow("FaceMesh Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()