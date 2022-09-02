import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

video = cv2.VideoCapture('../video/isabel.mp4')

with mp_pose.Pose(static_image_mode=True,) as pose:
    while True:
        ret, frame = video.read()
        if ret == False:
            break
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks is not None:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('pose', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
video.release()
cv2.destroyAllWindows()
