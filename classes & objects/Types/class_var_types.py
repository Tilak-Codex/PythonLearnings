                                                                                    #Types of classvariables
"""
        Types of variables
                                            Instance variable   -> initiasized within constructor  (uses self convention)
                                            class variable         ->  initialised in class(outside any  method) -> Common to all objects  (does not use self convention)
                                                                                 aka static variables   

"""

class Phone:
    chargertype="ctype"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand",self.brand)
        print("price",self.price)
       
samsung=Phone("samsung","1000")

samsung.display()
print(Phone.chargertype)
print(samsung.chargertype)


"""
            Memory for the static variables is allocated once object for the class is created
            They can be accessed using class_name.attribute_name (within and outside the class )
            objects can access their class variable
"""
