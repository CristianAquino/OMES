import cv2
import numpy as np


def dibujar(mask, color):
    contorno, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contorno:
        area = cv2.contourArea(c)
        if area > 3000:
            M = cv2.moments(c)
            if (M['m00'] == 0):
                M['m00'] = 1
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, f'{x},{y}', (x+10, y), font,
                        0.75, (0, 255, 0), 1, cv2.LINE_AA)
            nuevoContorno = cv2.convexHull(c)
            cv2.drawContours(frame, [nuevoContorno], 0, color, 3)


video = cv2.VideoCapture(0)

redBajo1 = np.array([0, 100, 20], np.uint8)
redAlto1 = np.array([8, 255, 255], np.uint8)

redBajo2 = np.array([175, 100, 20], np.uint8)
redAlto2 = np.array([179, 255, 255], np.uint8)

azulBajo = np.array([100, 100, 20], np.uint8)
azulAlto = np.array([125, 255, 255], np.uint8)

amarilloBajo = np.array([15, 100, 20], np.uint8)
amarilloAlto = np.array([45, 255, 255], np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = video.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
        maskAmarillo = cv2.inRange(frameHSV, amarilloBajo, amarilloAlto)
        maskRed = cv2.add(maskRed1, maskRed2)
        dibujar(maskRed, (0, 0, 255))
        dibujar(maskAzul, (255, 0, 0))
        dibujar(maskAmarillo, (0, 255, 255))
        cv2.imshow('VENTANA', frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

video.release()
cv2.destroyAllWindows()
