import cv2
import mediapipe as mp
import pydirectinput
import time
import os
import warnings

# -----------------------------
# Suppress TensorFlow/Mediapipe warnings
# -----------------------------
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')

# -----------------------------
# Mediapipe setup
# -----------------------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# -----------------------------
# Gesture control
# -----------------------------
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:

    prev_action = None  # to prevent repeated key presses

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        h, w, _ = image.shape
        start_time = time.time()

        # Flip and convert to RGB
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw middle line
        cv2.line(image, (w//2, 0), (w//2, h), (0, 255, 0), 2)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp.solutions.drawing_styles.get_default_hand_landmarks_style(),
                    mp.solutions.drawing_styles.get_default_hand_connections_style()
                )

                # Index finger tip
                index_finger_tip = hand_landmarks.landmark[8]
                index_x = int(index_finger_tip.x * w)

                # Gesture to key mapping
                if index_x > w // 2 + 50:
                    if prev_action != "right":
                        pydirectinput.keyDown('right')
                        pydirectinput.keyUp('left')
                        prev_action = "right"
                    cv2.putText(image, "ACCELERATION", (400, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

                elif index_x < w // 2 - 50:
                    if prev_action != "left":
                        pydirectinput.keyDown('left')
                        pydirectinput.keyUp('right')
                        prev_action = "left"
                    cv2.putText(image, "BRAKE", (400, 70),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
                else:
                    if prev_action is not None:
                        pydirectinput.keyUp('left')
                        pydirectinput.keyUp('right')
                        prev_action = None

        # FPS
        end_time = time.time()
        fps = int(1 / (end_time - start_time))
        cv2.putText(image, f'FPS: {fps}', (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display
        cv2.imshow("Gesture Control", image)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC to exit
            break

cap.release()
cv2.destroyAllWindows()