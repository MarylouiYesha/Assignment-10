import cv2
from pyzbar.pyzbar import decode

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
used_codes=[]

camera=True
while camera == True:
    success, frame = cap.read()

    for code in decode (frame):
        info=code.data.decode('utf-8')
        with open ("qrdata.txt", mode='w') as file:
            file.write(info)
    
    cv2.imshow("test", frame)
    cv2.waitKey(1)

     
camera.release()
cv2.destroyAllWindows()
