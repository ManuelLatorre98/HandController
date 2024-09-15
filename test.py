import cv2
import mediapipe as mp
import time
import HandController.handTracking as ht
import HandController.showImage as shi
import math
import numpy as np

hands_detector = ht.HandsDetector()
capture = cv2.VideoCapture(0)



while True:
    success, img = capture.read()
    img = hands_detector.find_hands(img)
    lm_list = hands_detector.find_position(img, 0, True)

    fingers_x=[]
    fingers_y=[]
    finger_tips_index = [8, 12, 16, 20]
    min_size = 90
    max_size = 270

    if len(lm_list):
        thumb_x, thumb_y= lm_list[4][1], lm_list[4][2]

        # This access only to the tips of fingers
        for idx in finger_tips_index:
            # Appends the coords of every finger except the thumb
            fingers_x.append(lm_list[idx][1])
            fingers_y.append(lm_list[idx][2])

        # Iterate over fingers to thumb
        for finger_num in range(len(finger_tips_index)):
            cv2.line(img, (fingers_x[finger_num], fingers_y[finger_num]), (thumb_x, thumb_y), (0, 0, 255), 3)
            cx, cy =( fingers_x[finger_num] + thumb_x) // 2, (fingers_y[finger_num] + thumb_y) // 2  # Gets the center
            # of line
            #cv2.circle(img, (cx, cy),15, (255, 0 , 255), cv2.FILLED)  # Draw a point at center of line
            # Iterate over the lengths between the fingers and thumb to search the shortly
            finger_to_thumb_length = math.hypot((fingers_x[0] - thumb_x), (fingers_y[0] - thumb_y))
            # Hand range 10 - 260
            # Stick range 90 - 260
            stick_range = np.interp(finger_to_thumb_length, [20, 260], [90, 270])
            print(stick_range)
            if finger_to_thumb_length < 40:
                cv2.circle(img, (cx, cy),15, (0, 255, 255), cv2.FILLED)  # Draw a point at center of line


        cv2.circle(img, (thumb_x, thumb_y), 15, (0, 255, 0), cv2.FILLED)



    shi.show_image(img)
