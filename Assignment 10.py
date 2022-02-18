import cv2
import webbrowser

reader=cv2.VideoCapture(0)
qrdetect=cv2.QRCodeDetector()

while True:
    _, img=cap.read()
    data,one, _=detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow('QRCODEscanner', img)
    if cv2.waitKey(1)== ord('q')
    break
b=webbrowser.open(str(a))
cap.release(a)
cv2.destroyAllWindows