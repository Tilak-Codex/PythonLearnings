                                                                            #Classes  & Objects

#Object
"""
        An object is any entity(which has its own identity) that has attributes and behaviour.
        Object is an instance(copy of class that you can interact eith, independenlty from other instances) of a class
        Attribute
                Name
                age
                color
                height
        Behaviour
                Walking
                running
                signing

#syntax     object_name=class_name()
"""
#class
"""class ->blue print of that object



#Syntax


        class class_name:
                class definition
                         (var and methods)
"""
#Variables inside a class is called as attribute (self.attribute=value)
#functions inside a class is called as Methods (they contain self as parameter)

#Constructor
"""
        def __init__(self):  is a constructor of a class
        It is used to initialise value to the attributes in a class
        It is called implicitly when instance of the class is created
        It is built-in function
        
"""
#self
"""
         refers to the instance of the class that is currently being used.
         it is used as first arg to the methods and constructor in a class(mandatory).
         When a method of an object is called, the object is automatically passed as first arg to the self parameter.
         This enables you to modify and access values of that instance 
"""


class Laptop:
    def __init__(self,price,ram,processor):
        self.price=price
        self.ram=ram
        self.processor=processor
    def display(self):
        print("Price of is: ",self.price)
        print("Ram of is: ",self.ram)
        print("Processor of is: ",self.processor)

hp=Laptop(20000,"6GB","i3")
dell=Laptop(30000,"6GB",'i3')


print(hp.display())   #Internally passed as hp.display(hp)
print(dell.display())

#if self is printed,it gives the memory location of the class
