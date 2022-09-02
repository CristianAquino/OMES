import cv2
from setting import get

video = cv2.VideoCapture(get('video1'))

while True:  # lee la imagen a cada momento
    ret, imagen = video.read()
    if ret == True:
        cv2.imshow('Video', imagen)
        # 0xff si se trabaja en maquina de 65 bits
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break  # ord tecla que detiene el proceso
video.release()  # cerrar la captura
cv2.destroyAllWindows()
