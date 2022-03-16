import cv2
import numpy as np
video = cv2.VideoCapture(0)

color_range = np.array([104 ,90 ,46 ,113 ,176 ,174])


while True:
    _,frame =video.read()

    hue_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hue_image,color_range[:3],color_range[3:])
    final = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('original', frame)
    cv2.imshow('mask',mask)
    cv2.imshow('final',final)

    if cv2.waitKey(1) ==13:
        break

video.release()
cv2.destroyAllWindows()
