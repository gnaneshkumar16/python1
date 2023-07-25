import pyqrcode
url="https://www.youtube.com/@tgbcrazy9716"
k=pyqrcode.create(url)
k.svg('qrcode.svg',scale=10)