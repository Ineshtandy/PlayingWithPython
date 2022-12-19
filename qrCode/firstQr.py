import qrcode

websiteLink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
# version is int from 1 to 40 controlling the size of qr code
# box size controls num of pixels in each box
# border controls how many boxes thick the border should be

qr.add_data(websiteLink)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('myfirstqr.png')
