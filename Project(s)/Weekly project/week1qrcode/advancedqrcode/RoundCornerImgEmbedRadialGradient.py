import qrcode
from qrcode.image.styledpil import StyledPilImage  #For embedding
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask  #For color

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('https://wa.me/919585198687')
qr.make_image(fit=True)
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage,color_mask=RadialGradiantColorMask(),embeded_image_path=r"C:\Users\DELL\Pictures\Saved Pictures\bubu-transparent.png")
img_3.save("bubuwhatsapp.png")
