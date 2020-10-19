import pyqrcode
import png
from pyqrcode import QRCode

url_link = input("Enter the desired URL for crearing QR code : \n")
url = pyqrcode.create(url_link)
# url.svg("horizon.svg", scale = 8)
url.png("qrcode.png", scale = 8)
print("QR Code for given URL generated!")