"""
Project: OpenCV Drawing Studio

Features:
- Detecting Cursor Coordinates
- Freehand Drawing (Circle,Line)
- Rectangle Drawing
- Save Drawing (Press 'S')
- Exit Application (Press 'ESC')

Author: Yuvraj Makani
"""


import cv2
import numpy as np

# CREATE A BLACK CANVAS
canvas = np.zeros((600,800,3),np.uint8)

# DRAWING STATE VARIABLES
drawing = False
prev_x,prev_y = -1,-1

# MOUSE CALLBACK FUNCTION
def mouse_event(event , x , y , flags , params):
    global prev_x,prev_y,drawing
    # FOR DRAWING CIRCLES
    # cv2.circle(canvas, (x, y), 3, (255, 255, 255), -1)

    # FOR DRAWING RECTANGLE
    # cv2.rectangle(canvas, pt1=(200, 200), pt2=(300, 300), color=(255, 0, 255), thickness=10)

    # FOR DRAWING LINES
    # Left Mouse Button Pressed
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     drawing = True
    #     prev_x, prev_y = x, y
    #
    # # Mouse Moving
    # elif event == cv2.EVENT_MOUSEMOVE:
    #
    #     if drawing:
    #         cv2.line(canvas,
    #                  (prev_x, prev_y),
    #                  (x, y),
    #                  (255, 0, 255),
    #                  3)
    #
    #         prev_x, prev_y = x, y
    #
    # # Left Mouse Button Released
    # elif event == cv2.EVENT_LBUTTONUP:
    #     drawing = False


    #FOR MOUSE COORDINATES
    # if event == cv2.EVENT_MOUSEMOVE:
    #  print(x,y)

# MAIN FUNCTION
cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas",mouse_event)

# MAIN APPLICATION LOOP
while True:
    cv2.imshow("Canvas",canvas)
    key = cv2.waitKey(1)

    # PRESS "S" TO SAVE OUTPUTS
    if key == ord('s'):
        cv2.imwrite("outputs/my_drawing.png", canvas)
        print("Image Saved!")

    if key==27:                  #ESC
        break
cv2.destroyAllWindows()





