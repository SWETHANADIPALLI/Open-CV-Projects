import cv2
import os
parent_directory=os.getcwd()
dataset="dataset"
path=os.path.join(parent_directory,dataset)
if not os.path.isdir(path):
    os.mkdir(path)
(Width,Height)=(100,100)
alg="haarcascade_frontalface_alt.xml"
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + alg)
cam=cv2.VideoCapture(0)
count=1
tc=1
while tc<=30:
    text='No Face Detected'
    img=cam.read()[1]
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grayImg, scaleFactor=1.05,minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        faceOnly=grayImg[y:y+h,x:x+h]
        resizeImg=cv2.resize(faceOnly,(Width,Height))
        cv2.imwrite('%s/%s.jpg'%(path,tc),resizeImg)
        text='Face Detected'
    if text=='No Face Detected':
        count+=1
        text=text+str(count)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow('Face Detection',img)
    tc+=1
    key=cv2.waitKey(10)
    if key==24:
        break
cam.release()
cv2.destroyAllWindows()
        
