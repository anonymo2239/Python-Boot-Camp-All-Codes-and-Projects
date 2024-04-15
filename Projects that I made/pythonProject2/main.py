import qrcode

data = 'https://github.com/anonymo2239'
img = qrcode.make(data)
img.save('BenimQRkodum4.png')