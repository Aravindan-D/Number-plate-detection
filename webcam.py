#ML CODE FOR IMAGE CAPTIRING AND LICENSE PLATE RECOGNITION
#IMPORTING REQUIRED PACKAGES
import cv2
import PIL
import pytesseract
import pandas as pd
import imutils
import numpy as np
import os

#INITIALIZING IMAGE COUNTER
img_counter = 0
while True:
    cam = cv2.VideoCapture(0) #camera ON

    cv2.namedWindow("Camera") #open a window

    ret, frame = cam.read()  #read Input from camera
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Camera", frame)  #show the pop up dialog box called Camera
    #WAITS FOR 5 SECONDS
    k = cv2.waitKey(5)
    if k%256 == 27:
        # ESC pressed it will close all the program
        print("Escape hit, closing...")
        #CLOSES THE CAMERA WINDOW
        cam.release()
        cv2.destroyAllWindows()
        break
    elif k%256 == 32:
        # SPACE pressed captures image
        # IMAGE NAME THAT SHOULD BE SAVED
        img_name = "opencv_frame_{}.png".format(img_counter)
        #SETTING PATH FOR SAVING THE IMAGE IN RESPECTIVE LOCATION
        path='D:\Captured Images'
        #SAVING THE IMAGE
        cv2.imwrite(os.path.join(path ,img_name),frame)
        #PRINTING THE IMAGE IS SAVED
        print("opencv_frame_"+str(img_counter)+'written!',end=" ")
        #READS THE CAPTURED IMAGE
        img = cv2.imread('D://Captured Images'+'//opencv_frame_'+str(img_counter)+'.png',cv2.IMREAD_COLOR)
        cv2.imshow('image',img)
        #IMCREMENTS COUNTER
        img_counter += 1
        
