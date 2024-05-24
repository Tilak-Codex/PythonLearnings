                                                                            #Exception handling
#try
"""
        critical statements are written in try block
"""

#except
"""
        Statements to be executed after exception encountered
"""
#finally
"""
Statements to be executed after expection is handled , it is excetued in both situation such as error and not error
"""
"""
try:
    a=int(input("Enter a number:"))
    b=int(input("Enter another number:"))
    c=a+b
    print(c)
except Exception:                 #handles all exception from exception class to handle specific exception give their class ValueError,KeyError etc
    print("Exception")
"""
"""
try:
    a=(input("Enter a number:"))
    b=(input("Enter another number:"))
    c=a/b
    print(c)
except Exception as e:    #exception object e contains the exception description raised                 
    print("Exception",e)
"""
#A try block can contain any number of except block 
try:
   print(d)
except Exception as e:    #exception object e contains the description of exception  raised  in  the snippet
    print("Exception",e)


#To handle all exceptions use except: only not except Exception as e:
