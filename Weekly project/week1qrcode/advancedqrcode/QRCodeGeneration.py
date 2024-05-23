#Advanced

import qrcode 

#Setting functionality of  qrcode using class called QRCode
 
functionality=qrcode.QRCode(version=1,
                            error_correction=qrcode.constants.ERROR_CORRECT_H,
                            box_size=10,border=4)

#Creating qrcode with given functionality

functionality.add_data("https://wa.me/919585198687")

functionality.make(fit=True)  #Ensures that 

img=functionality.make_image(fill_color="green",back_color="white")

#Saving image

img.save("Whatsapplink.png")
