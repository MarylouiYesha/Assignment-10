import cv2

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
        break

cap.release(a)
cv2.destroyAllWindows()

