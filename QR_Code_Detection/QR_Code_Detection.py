import cv2
from pyzbar.pyzbar import decode
import numpy as np
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,4)
saved = "12345" #Customer Who Ordered
while True:
    success,img=cap.read()

    decodedObjects=decode(img)

    for obj in decodedObjects:
        myData=obj.data.decode('utf-8')
        print(myData)
        pts = np.array([obj.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2=obj.rect
        if(saved==myData): #matching scanned QR-Code with the Saved code above
            cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),3)
    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
