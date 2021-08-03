import qrcode
import image

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5,
)

data = 'https://www.youtube.com/channel/UCLYAvOLIC0vYV9mnIaqXLXQ'

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="blue", back_color ="white")

img.save("qr.png")
