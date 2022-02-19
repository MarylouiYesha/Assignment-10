import cv2
import numpy as np
from pyzbar.pyzbar import decode


with open ("qrdata.txt", mode='w') as file:
    file.write("Recognized Code")
reader=cv2.VideoCapture(2)

while True:
    success, img = reader.read()

    if not success:
        break

    for code in decode(img):
        print (code.data.decode("utf-8"))
    
    cv2.imshow("test", img)
    cv2.waitKey(1)

    
