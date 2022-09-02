import cv2
from setting import get

imagen1 = cv2.imread(get('img5'))
imagen2 = cv2.imread(get('img5'), 0)
_, th = cv2.threshold(imagen2, 240, 255, cv2.THRESH_BINARY_INV)
contorno, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_SIMPLEX
i = 0
for c in contorno:
    M = cv2.moments(c)
    if (M['m00'] == 0):
        M['m00'] = 1
    x = int(M['m10']/M['m00'])
    y = int(M['m01']/M['m00'])

    mensaje = f'NUM: {i+1}'
    cv2.putText(imagen1, mensaje, (x, y), font,
                0.75, (255, 0, 255), 2, cv2.LINE_AA)
    # 1 = uno por uno los contornos
    cv2.drawContours(imagen1, [c], 0, (0, 255, 0), 2)
    cv2.imshow('POLIGONOS', imagen1)
    cv2.waitKey(0)
    i = i+1
cv2.destroyAllWindows()
