import pyqrcode
import png
url=input("Enter the url: ")
QR=pyqrcode.create(url)
QR.png("QR.png",scale=8)



