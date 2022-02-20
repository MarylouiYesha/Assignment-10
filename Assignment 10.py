from datetime import datetime
import cv2
from pyzbar import pyzbar

def read_qrcodes(frame):
    qrcodes = pyzbar.decode(frame)
    for qrcode in qrcodes:
        a, b , c, d = qrcode.rect

        today = datetime.now()              
        time_ = today.strftime("%H:%M")
        date_ = today.strftime("%B %d, %Y")

        qrcode_info = qrcode.data.decode('utf-8')
        cv2.rectangle(frame, (a, b), (a+c, b+d), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, "CONTACT TRACING", (a + 6, b - 6), font, 1.0, (0,0,0), 1)

        with open("contacttracinginformation.txt", mode ='w') as file:
            file.write(qrcode_info + (f"\n\n\nDate: {date_}\nTime: {time_}"))
    return frame
    
def main():
    camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = read_qrcodes(frame)
        cv2.imshow('QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    camera.release()
    cv2.destroyAllWindows()

main()