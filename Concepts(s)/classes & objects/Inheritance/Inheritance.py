class granpa():
    def car(self):
        print("drive car")
        
class dad(granpa):
    def phone(self):
        print("Dad's Phone")

class mom():
    def cook(self):
        print("sweet")

class son(dad,mom):
    def laptop(self):
        print("son's Laptop")


ram=son()
ram.laptop()
ram.phone()
ram.cook()
ram.car()
"""
The child class can access all the attributes and methods of the parent class
but parent class cannot access the child class
if one child class has only one parent class -> Single inheritance
one child class , multiple parent class -> Multiple inheritance
if a class is derived from another child  class ->Multi level inheritance
One parent class multiple child class -> heiarchial inheritance
Hybrid inheritance -> consists all many types of inheritance
"""
