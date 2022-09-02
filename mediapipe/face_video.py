import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_face_detection.FaceDetection(min_detection_confidence = 0.5) as face_detection:
    while True:
        ret, frame = video.read()
        if ret == False:
            break
        frame = cv2.flip(frame,1)
        image_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)
        if results.detections is not None:
            for detection in results.detections:
                mp_drawing.draw_detection(frame,detection)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
video.release()
cv2.destroyAllWindows()