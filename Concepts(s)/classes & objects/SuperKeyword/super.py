"""
        When an object is created for a class -> The constructor of the class is executed automatically

        During Inheritance

        Case I : Child class does not have Constructor but parent class has.

                    Parent class constructor is executed

        Case II : Child class and Parent class both have constructor

                    Child class constructor is executed


When we want to call constructor of parent class using child class object we use super().__init__()

In case of multiple inheritance first parent class constructor is accessed using super().__init__()
"""


class a():
    def __init__(self):
        print("a class constructor")
    def met(self):
        print("method of a")

class b(a):
    def __init__(self):
        #super().__init__()
        #super().met()
        print("b class constructor")
    def met(self):
        print("method of b")
        super().__init__()


B=b()
B.met()


"""
    NOTE
            We can access any other attibute or method in the parent class which is same
"""
    
