import cv2
import numpy as np
import imutils
from setting import get

imagen = cv2.imread(get('img2'))
ancho = imagen.shape[1]  # columnas
alto = imagen.shape[0]  # filas

# TRASLACION
M1 = np.float32([[1, 0, 10], [0, 1, 100]])  # 10,100 son respectivamente x,y
# aplica la transformacion a una imagen
salida1 = cv2.warpAffine(imagen, M1, (ancho, alto))
# M es matriz de transformacion
# ROTACION DE IMAGEN CON TECLADO
for i in range(360):
    # ROTACION
    # con el '/2'rotan las aspas
    M2 = cv2.getRotationMatrix2D((ancho/2, alto/2), i, 1)
    salida2 = cv2.warpAffine(imagen, M2, (ancho, alto))
    cv2.imshow('SALIDA2', salida2)
    if cv2.waitKey(0) & 0x0FF == 27:
        break

# ESCALADO-RECOMENDADO IMULTIS(se ingresa una medida, se calcula la segunda)
salida3 = imutils.resize(imagen, width=600)

# RECORTE
salida4 = imagen[150:300, 200:400]  # [f_inicial:f_final,c_inicial:c_final]
cv2.imshow('ENTRADA', imagen)
cv2.imshow('SALIDA1', salida1)
cv2.imshow('SALIDA3', salida3)
cv2.imshow('SALIDA4', salida4)
cv2.waitKey(0)
cv2.destroyAllWindows()
