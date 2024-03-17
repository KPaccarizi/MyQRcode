import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make('https://www.linkedin.com/in/kpacarizi/')
myqr1 = qrcode.make('https://www.google.com/')

myqr.save("myqr.png", scale = 8)
myqr1.save("myqr1.png", scale = 9)

b = decode(Image.open('myqr.png'))
print(b[0].data.decode("ascii"))