import cv2
import mediapipe as mp
import time
 
 
class hand_detector():
    def __init__(self, max_hands=2, mp_mode=False, detect_con=0.5, track_con=0.5):
        self.mode = mp_mode
        self.max_hands = max_hands
        self.detect_con = detect_con
        self.track_con = track_con

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands,
                                         self.detect_con, self.track_con)
        self.mp_draw = mp.solutions.drawing_utils