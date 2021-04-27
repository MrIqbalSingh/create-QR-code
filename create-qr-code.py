import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("PLACE YOUR TEXT HERE")
qr.png("myQRCode.png", scale=16)

d = decode(Image.open("myQRCode.png"))
print(d[0].data.decode("ascii"))