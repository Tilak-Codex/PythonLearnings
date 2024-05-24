                                                                    #Custom exceptions
#Rasing Exceptions when needed...
"""a=int(input("Enter a number between 5 and 9"))
if(a<5 or a>9):
    raise ValueError("You should provide value between 5 and 9") 

"""
#User defined exception

#Note that the statmements in the defined exception are excecuting automatically so use only pass...(may vary)

class TooSmallError(Exception):
    #If needed write your needed snippet or add pass statement
    # print("Hello")

class TooLargeError(Exception):
    #print("Hi")
    pass

""" Here we are going to create a game of gussing the correct number"""

num=10
while True:
    try:
        ch=int(input("Enter a random number"))
        if ch < num:
            raise TooSmallError("The number is too small")
        elif ch>num:
            raise TooLargeError("The number is too large")
        break
    except TooSmallError:
        print("You have entered a smaller number please try again")
    except TooLargeError:
        print("You have entered a larger number please try again")
print("Congrats!!You found the correct number")

#Now We have to define both the user defined exceptions such as TooSmallError and TooLargeError which is on top

