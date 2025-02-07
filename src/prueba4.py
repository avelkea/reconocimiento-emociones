import cv2
import dlib
import mediapipe as mp
import numpy as np
import math

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

mpDibujo = mp.solutions.drawing_utils
ConfDibu = mpDibujo.DrawingSpecthickness=1, circle_radius=1

mpMallaFacial = mp.solutions.face_mesh
MallaFacial = mpMallaFacial.FaceMesh(max_num_faces=1)

while True: 

    ret,frame = cap.read()

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultados = MallaFacial.process(frameRGB)

    px = []
    py = []
    lista = []
    r = 5
    t = 3

    if resultados.multi_face_Landmarks:
        for rostros in resultados.multi_face_landmarks:
            mpDibujo.draw_landmarks(frame, rostros, mpMallaFacial.FACE_CONNECTIONS, ConfDibu, ConfDibu)

            for id.puntos in enumerate(rostros.Landmark):
                al, an, c = frame.shape
                x,y = int(puntos.x*an), int(puntos.y*al)
                px.append(x)
                py.append(y)
                lista.append([x,y])
                if len(lista) == 468:
                    #ceja derecha
                    x1, y1 = lista[65][1:]
                    x2, y2 = lista[158][1:]
                    cx, cy = (x1+x2)//2, (y1+y2)//2
                    cv2.line(frame, (x1, y2), (x2, y2), (0, 0, 0), t)
                    cv2.circle(frame, (x1, y1), r, (0, 0, 0), cv2.FILLED)
                    cv2.circle(frame, (x2, y2), r, (0, 0, 0), cv2.FILLED)
                    cv2.circle(frame, (cx, cy), r, (0, 0, 0), cv2.FILLED)
                    longitud = math.hypot(x2 - x1, y2 - y1)
                    #print(longitud)

                    #ceja izquierda
                    x3, y3 = lista[295][1:]
                    x4, y4 = lista[385][1:]
                    cx2, cy2 = (x3+x4)//2, (y3+y4)//2
                    longitud2 = math.hypot(x4 - x3, y4 - y3)
                    #print(longitud2)


                    #boca 
                    x5, y5 = lista[78][1:]
                    x6, y6 = lista[308][1:]
                    cx3, cy3 = (x5 + x6)//2, (y5 + y6)//2
                    longitud3 = math.hypot(x6 - x5, y6 -y5)
                    #print(longitud3)

                    #apertura de la boca
                    x7, y7 = lista[13][1:]
                    x8, y8 = lista[14][1:]
                    cx4, cy4 = (x7 + x8)//2, (y7 + y8)//2
                    longitud4 = math.hypot(x8 - x7, y8 - y7)
                    #print(longitud4)


                    if longitud < 18 and longitud2 <19 and longitud3 >80 and longitud3 < 95 and longitud4 <5:
                        cv2.putText(frame, 'Persona Enojada', (480, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 3)
                        
                    #feliz
                    elif  longitud > 20 and longitud1 < 30 and longitud2 > 20 and longitud2 < 30 and longitud3 > 109 and longitud4 > 10 and longitud4 < 20:
                        cv2.putText(frame, 'Persona Feliz', (480, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 3)
                        
                    #triste
                    elif longitud > 20 and longitud < 35 and longitud2 > 20 and longitud2 < 35 and longitud3 > 80 and longitud3 < 95:
                        cv2.putText(frame, 'Persona Triste', (480, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 3)
                        
            cv2.imshow("Reconocimiento de emociones",frame)
            t = cv2.waitkay(1)

            if t == 27:
                break

            cap.release()
            cv2.destroyAllWindows()