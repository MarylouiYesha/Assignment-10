import cv2
from pyzbar import pyzbar

def qrcode(frame):
    with open ("qrdata.txt", mode='w') as file:
        file.write("Recognized Code")

    return frame

def qrfinal():
    reader=cv2.VideoCapture(0)
    ret, frame=reader.read()
    
    while ret:
        ret, frame=reader.read()
        frame = qrcode(frame)
        cv2.inshow('QR reader', frame)
        if cv2.waitKey(1) & 0xFF==27:
            break
    
    reader.release()
    cv2.destroyAllWindows()

qrfinal()
