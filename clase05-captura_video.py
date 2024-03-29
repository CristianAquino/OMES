import cv2

video = cv2.VideoCapture(0)  # cero xq es camara web
# grabar video
salida = cv2.VideoWriter('video/VideoPrueba.avi',
                         cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))
# cv2.VideoWriter(nombre,codec,fotogramas,dimension)

while True:  # lee la imagen a cada momento
    ret, imagen = video.read()
    if ret == True:
        cv2.imshow('Video', imagen)
        salida.write(imagen)
        # 0xff si se trabaja en maquina de 65 bits
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break  # ord tecla que detiene el proceso
video.release()  # cerrar la captura
salida.release()
cv2.destroyAllWindows()
