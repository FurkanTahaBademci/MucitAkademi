# STEP 1: Import the necessary modules.
print("Gerekli kütüphaneler yükleniyor...")

import mediapipe as mp
import cv2
import numpy as np

print("Gerekli kütüphaneler yüklendi.")
# STEP 2: Initialize MediaPipe Hands

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

print("MediaPipe Hands başlatıldı.")
("MediaPipe Hands başlatıldı.")
# STEP 3: Create Hands object
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
print("Hands nesnesi oluşturuldu.")
# STEP 4: Initialize webcam
cap = cv2.VideoCapture(0)

print("El hareketleri algılanıyor...")
print("Çıkmak için 'q' tuşuna basın")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # BGR to RGB conversion
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Hand detection
    results = hands.process(rgb_frame)
    
    # Draw hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
    
    # Display frame
    cv2.imshow('El Hareketleri Algılama', frame)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()