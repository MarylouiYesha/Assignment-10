import cv2


reader=cv2.VideoCapture(0)
qrdetector=cv2.QRCodeDetector()
while True:
    _,img=reader.read()
    data,one,_=qrdetector.detectAndDecode(img)
    if data:
        a=data
        break 
    cv2.imshow('qrscanner',img)
    if cv2.waitKey(1)==ord('q'):
        break

reader.release()
cv2.destroyAllWindows
