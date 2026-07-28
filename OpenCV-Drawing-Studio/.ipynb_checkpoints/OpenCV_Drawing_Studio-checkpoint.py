import cv2
import numpy as np 

canvas = np.zeros((800,600,3),np.uint8)
cv2.imshow("Canvas", blank_space)
cv2.waitKey(0)
cv2.destroyAllWindows()


def mouse_event(event , x , y , flags , params):
    print(x,y)