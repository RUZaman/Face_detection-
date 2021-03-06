#face detection program


import cv2
import numpy as np


scale_factor = 1.1
min_neighbors = 3
min_size = (30, 30)

#load pre trainned model for face detection
cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#initialize camera
cap=cv2.VideoCapture(0) #put 'video2.MP4' instead of 0 for video file input
cap.set(3,360)
cap.set(4,480)



while True:
     check,img=cap.read()
     #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     #faces=cascade.detectMultiscale(img,1.1,3,(30,30))
     faces=cascade.detectMultiScale(img, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                              minSize=min_size)

     #draw ractangle around faces
     for(x,y,a,b) in faces :
         cv2.rectangle(img,(x,y),(x+a,y+b),(0,255,0),8)
         cv2.imshow("img",img)
     #Press q to quit the running program
     if cv2.waitKey(1) & 0xFF == ord('q'):
             break
cap.release()
cv2.destroyAllWindows()
               
