import cv2
from setting import get


def onChange(val):
    pass


imagen = cv2.imread(get('img7'))
cv2.namedWindow('G')
cv2.createTrackbar('value', 'G', 0, 15, onChange)

while True:
    val = cv2.getTrackbarPos('value', 'G')
    if val > 0:
        imagenN = cv2.blur(imagen.copy(), (val, val))
    else:
        imagenN = imagen.copy()
    cv2.imshow('G', imagenN)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()
