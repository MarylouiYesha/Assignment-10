import cv2
from datetime import datetime

today = datetime.now()              
time_ = today.strftime("%H:%M")
date_ = today.strftime("%B %d, %Y")
    
cap=cv2.VideoCapture(0)
detector=cv2.QRCodeDetector()

while True:
    _, img=cap.read()
    data,one,_=detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow('QR READER', img)
    if cv2.waitKey(1)==ord('q'):
        with open ("QR Info.txt", mode='w')as file:
            file.write(data+(f"\n\n\nDate: {date_}\nTime: {time_}"))
        
cap.release(a)
cv2.destroyAllWindows()

