# Python program for Detection of a 
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera

 
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0) 
 
# This drives the program into an infinite loop.
while(1):       
    # Captures the live stream frame-by-frame
    _, frame = cap.read()
    canvas = frame.copy()
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([5,120,120])
    upper_red = np.array([127,255,255])
 
# Here we are deresfining range of bluecolor in HSV
# This creates a mask of blue coloured 
# objects found in the frame.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    cv2.rectangle(mask, (200, 200), (300, 30), (255,0,0), 2)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    blob = max(contours, key=lambda el: cv2.contourArea(el))
    M = cv2.moments(blob)
    
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    cv2.circle(canvas, center, 2 ,(0,0,255), -1)
    print(center)
    
     
# The bitwise and of the frame and mask is done so 
# that only the blue coloured objects are highlighted 
# and stored in res
    #rTypeError: img is not a numerical tuplees = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('can',canvas)

 
# This displays the frame, mask 
# and res which we created in 3 separate windows.
    k = cv2.waitKey(5)
    if k == 27:
        break
 
# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
 
# release the captured frame
cap.release()
