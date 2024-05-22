#Functions are also objects
#So objects can be passed as argument to a function.
#we can create alias for function

#Higher Order Functions

"""
        
        Functions that can accept other functions as arguments are also called as higher order functions

"""
#adding two numbers

def sum_up(x,y):
    return x+y

def do_something(foo,a,b):      #This is Higher order function   takes function and its argument as paramemter
    result=foo(a,b)
    return result

print(do_something(sum_up,5,4))
