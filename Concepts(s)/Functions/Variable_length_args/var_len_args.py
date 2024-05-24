#variable length argument 

#*args
"""
    
    Used when we dont know the number of args we needed
    eg:- add()
            First-> i have to add two numbers
            Second -> i have to add three times and so on

            I cannot keep on editing the number of args in the function definition so we use *args
args are receivd as tuple
It accepts only non-keyword arguments
If we want to accept keyword arguments then **kwargs is used
"""
sum=0
def add(*args):
    global sum
    for i in args:
        sum+=i
    return sum

result=add(4,5,5)
print(result)

#**kwargs
"""
    Consider a form which consists of following :- Name,Ph.no,adddress,Nationality,State
    We got two clients Alice and Bob
    Alice is convinced only to pass values to fields such as Name,address,Nationality and state
    Bob is ready to pass values to all the fields
    In such case we have to use variable length keywored argument hence **kwargs is used
"""

#Remark
""" Here i found someting you can access a global variable anywhere in a function
       But to modify its value in any other scope, you have to declare it using the keyword global
       use global var    in that scope and modify the value
       We cannot use that variable before global var statement
"""
