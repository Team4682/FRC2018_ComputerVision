import cv2
import numpy as np
from time import sleep
from networktables import NetworkTables as nt
import math

cap = cv2.VideoCapture(0)
ip = "10.46.82.2"
sd = nt.getTable("SmartDashboard")
sc = nt.getTable("Scale")
s = nt.getTable("Switch")
centerX = 320
centerY = 225
def valueChanged(table, key, value, isNew):
     print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key,value, isNew))

def connectionListener(connected, info):
     print(info, '; connected=%s' % connected)

def computeCenter(M):
    m00 = int(M["m00"])
    m10 = int(M["m10"])
    m01 = int(M["m01"])
    
    if m00 == 0:
        print("Detected bad data from opencv")
        return (-1, -1)
    else:
        x = int(m10/m00)
        y = int(m01/m00)
        #print(x)
        #print(y)
        return(x,y)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    canvas = frame
    
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130,255, 255])
    lower_red = np.array([160, 100, 100])
    upper_red = np.array([179, 255, 255])
    
    
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cnt = cv2.findContours(dst.copy())
    imge = frame
    
    blob = max(contours, key=lambda el: cv2.contourArea(el), default=0)
    M = cv2.moments(blob)
    if (len(contours) == 0):
        print("Empty contours")
    else:
        pass
    
   

        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    center = computeCenter(M)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 100, minRadius=10, maxRadius=45)
    if circles is None:
        print("No Circles!")
        
    else:
        circles = np.round(circles[0, :]).astype("int")
        for(x,y, r) in circles:
            cv2.circle(canvas, (x, y), r, (255, 255, 0), 4)
            cv2.rectangle(canvas, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            
            
            
    cv2.circle(canvas, center, 2 ,(0,255,0), -1)
    x, y = center
    cv2.imshow('Mask', mask)
    cv2.imshow('Can', canvas)
    k = cv2.waitKey(33)
    if k == ord('a'):
        break
cap.release()
cv2.destroyAllWindows()
