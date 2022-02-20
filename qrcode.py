import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
used_codes=[]

camera=True
while camera == True:
    success, frame = cap.read()
    today = datetime.now()              
    time_ = today.strftime("%H:%M")
    date_ = today.strftime("%B %d, %Y")

    for code in decode (frame):
        info=code.data.decode('utf-8')
        with open ("qrdata.txt", mode='w') as file:
            file.write(info + (f"\n\n\nDate: {date_}\nTime: {time_}"))
        
    cv2.imshow("test", frame)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()