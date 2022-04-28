import cv2
import numpy as np


def test(x, b):
    gs_frame = cv2.GaussianBlur(x, (5, 5), 0)
    hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)
    erode_hsv = cv2.erode(hsv, None, iterations=2)
    inRange_hsv = cv2.inRange(erode_hsv, color_dist[b]['Lower'], color_dist[b]['Upper'])
    cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    try:
        c = max(cnts, key=cv2.contourArea)
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        center_x = int((box[0][0] + box[2][0]) / 2)
        return center_x
    except ValueError:
        return -1


ball_color = 'green'
color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
              }

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    test(frame, ball_color)
