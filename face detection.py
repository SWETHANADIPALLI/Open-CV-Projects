import cv2
import os
alg="haarcascade_smile.xml"
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + alg)
cam=cv2.VideoCapture(0)
count=1
while True:
    text='No smile Detected'
    img=cam.read()[1]
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grayImg, scaleFactor=1.05,minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text='Smile Detected'
    if text=='No smile Detected':
        count+=1
        text=text+str(count)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow('Smile Detection',img)
    key=cv2.waitKey(10)
    if key==24:
        break
cam.release()
cv2.destroyAllWindows()
        
