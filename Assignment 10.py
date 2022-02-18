import cv2
from pyzbar import pyzbar

def qrcode(frame):
    qrcodes = pyzbar.decode(frame)
    for qrcode in qrcodes:
        z, y , x, w = qrcode.rect

        qrcode_info=qrcode.data.decode('utf-8')
        cv2.rectangle(frame, (z, y)), (z+x, y+w), (0, 255, 0), 2

        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, "CONTACT TRACING", (z + 6, y - 6), font, 1.0, (0,0,0), 1)
        
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
