import cv2
import os
import numpy as np
from setting import get

# emoticones


def emotion(emotion):
    if emotion == 'sonrisa':
        img = cv2.imread(get('sonrisa'))
    if emotion == 'diablito':
        img = cv2.imread(get('diablito'))
    if emotion == 'molesta':
        img = cv2.imread(get('molesta'))

    return img


dataPath = 'img/caras_video'
peopleList = os.listdir(dataPath)
print(peopleList)

# el modelo que se esta utilizando
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# ubicacion del modelo xml o yaml
face_recognizer.read('img/models/modeloFace.xml')

video = cv2.VideoCapture(get('video1'))

faceClassif = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret, frame = video.read()
    if ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    # para las imagenes
    # se crea un frame para colocarlas ahi
    # las imagenes tiene que tener por lo menos el mismo alto que el video
    nFrame = cv2.hconcat(
        [frame, np.zeros((360, 270, 3), dtype=np.uint8)])  # alto,ancho

    face = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face:
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        # agregamos predict y colocamos el rostro que vamos a identificar
        # ademas brinda coordenadas para realizar una mejor identificacion
        result = face_recognizer.predict(rostro)

        # cv2.putText(frame,f'{result}',(x,y+5),1,1.3,(255,255,0),1,cv2.LINE_AA)

        # ajustar de acorde a lo mostrado por result
        if result[1] < 100:
            cv2.putText(
                frame, f'{peopleList[result[0]]}', (x, y), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
            # colocamos la funcion de las imagenes
            imagen = emotion(peopleList[result[0]])
            # para visualizar las img en el nuevo frame
            nFrame = cv2.hconcat([frame, imagen])

    cv2.imshow('PRUEBA', nFrame)

    k = cv2.waitKey(1)
    if k == ord('x'):
        break

video.release()
cv2.destroyAllWindows()
