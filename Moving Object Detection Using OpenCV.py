#Moving Object Detection Using OpenCV
import cv2
import time
import imutils
firstFrame=None
area=500
cam=cv2.VideoCapture(0)
time.sleep(1)
count=0
while True:
    _,img=cam.read()
    text='Normal'
    resizedImage=imutils.resize(img,width=500)
    grayImage=cv2.cvtColor(resizedImage,cv2.COLOR_BGR2GRAY)
    guassianImage=cv2.GaussianBlur(grayImage,(21,21),0)
    if firstFrame is None:
        firstFrame=guassianImage
        continue
    imgDiff=cv2.absdiff(firstFrame,guassianImage)
    thresholdImage=cv2.threshold(imgDiff,120,250,cv2.THRESH_BINARY)[1]
    thresholdImage=cv2.dilate(thresholdImage,None,iterations=2)#to reduce line thickness
    cnts=cv2.findContours(thresholdImage.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c)<area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        count=count+1
        text='Moving Object is detected '+str(count)+' times'

    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
    cv2.imshow('Video Stream',img)
    key=cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
        
