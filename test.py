import qrcode

qr = qrcode.make('https://youtube.com')
qrc = qrcode.QRCode()
qr.save('static/images/myQR.png')
