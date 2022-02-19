import pyqrcode
import pandas as pd


def createQRCode():
    df = pd.read_csv("qr.csv")

    for index, values in df.iterrows():
        print(values)

        image=pyqrcode.create()
        image.svg

createQRCode()


