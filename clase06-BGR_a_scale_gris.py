import cv2
from setting import get

bgr = cv2.imread(get('img2'))
gris = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

cv2.imshow('GRISES', gris)
cv2.waitKey(0)
cv2.destroyAllWindows()
