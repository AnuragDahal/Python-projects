import pyqrcode
import png
img=input("Enter the name of the image: ")
url=input("Enter the url: ")
QR=pyqrcode.create(url)
QR.png(f"{img}.png",scale=8)



