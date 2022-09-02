import cv2
import imutils
from setting import get

imagen = cv2.imread(get('img3'), 0)
imagen = imutils.resize(imagen, width=600)

# cuando sea mayor al umbral toma el color del umbral, si no cumple toma color original
_, truncate = cv2.threshold(imagen, 150, 255, cv2.THRESH_TRUNC)

cv2.imshow('M', imagen)
cv2.imshow('TRUNCATE', truncate)
cv2.waitKey(0)
cv2.destroyAllWindows()
