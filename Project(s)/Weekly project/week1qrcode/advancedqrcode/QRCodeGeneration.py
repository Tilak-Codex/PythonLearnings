#Advanced

import qrcode 
from qrcode.image.styledpil import StyledPilImage
#Setting functionality of  qrcode using class called QRCode
 
functionality=qrcode.QRCode(version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_H,
                            box_size=10,border=4)

#Creating qrcode with given functionality

functionality.add_data("https://wa.me/919585198687")

functionality.make(fit=True)  #Ensures that 

#img=functionality.make_image(fill_color="red",back_color="white")

img_3 = functionality.make_image(image_factory=StyledPilImage,embeded_image_path=r"C:\Users\DELL\Pictures\Saved Pictures\bubu-transparent.png")
#Saving image

img_3.save("MyWhatsappQR.png")
