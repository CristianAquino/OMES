import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# video = cv2.VideoCapture('../video/isabel.mp4')
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1) as face_mesh:
    while True:
        ret, frame = video.read()
        if ret == False:
            break
        frame = cv2.flip(frame, 1)
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        if results.multi_face_landmarks is not None:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION, mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1), mp_drawing.DrawingSpec(color=(255, 0,  255), thickness=1))
        cv2.imshow('face', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
video.release()
cv2.destroyAllWindows()
