import cv2
import imutils
from setting import get

imagen1 = cv2.imread(get('img4'))
imagen1 = imutils.resize(imagen1, width=500, height=400)

imagen2 = cv2.imread(get('img3'))
imagen2 = imutils.resize(imagen2, width=500, height=400)

adicion1 = cv2.add(imagen1, imagen2)
adicion2 = cv2.addWeighted(imagen1, 0.5, imagen2, 0.5, 0)

cv2.imshow('ADD', adicion1)
cv2.imshow('ADDWEIGHTED', adicion2)

cv2.waitKey(0)
cv2.destroyAllWindows()
