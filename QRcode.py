#libraries
import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

data = "https://play.google.com/store/apps/details?id=com.naukriGulf.app"
qr.add_data(data)
qr.make(fit = True)

img = qr.make_image(fill = "blue" , back_color = "white")
img.save("Nukri.png")
