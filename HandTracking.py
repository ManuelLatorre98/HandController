import cv2
import mediapipe as mp



class HandsDetector():
    def __init__(self, mode=False, max_hands=2, detection_conf=0.5, tracking_conf=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_conf = detection_conf
        self.tracking_conf = tracking_conf
        #HANDS
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_conf,
            min_tracking_confidence=self.tracking_conf
        )
        self.mp_draw = mp.solutions.drawing_utils #Draws

    def find_hands(self, img, draw = True):
        #Transform image from BGR to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.hands_results = self.hands.process(img_rgb)

        if self.hands_results.multi_hand_landmarks:
            for handLms in self.hands_results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS) #draws the landsmarks
        return img

    def find_position(self, img, hand_num=0, draw=True, draw_points_ids=[]):
        lm_list = []
        if self.hands_results.multi_hand_landmarks:
            my_hand = self.hands_results.multi_hand_landmarks[hand_num]
            for id, lm in enumerate(my_hand.landmark):
                height, width, channels = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height) #Coordenadas en px de cada landmark
                lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)

                if draw_points_ids:
                    if id in draw_points_ids:
                        cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        return lm_list




