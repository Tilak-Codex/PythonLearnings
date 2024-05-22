                                                        #import statement

#syntax :-   import module_name


#To access the methods in that module use module_name.function_name()


#To import methods selectively use from keyword

"""
        from module import method1,method2,etc

        now there is no  need to use the method using module.method ,you can directly use them
"""

#To import all varables, methods use from math import *  (not recommanded)


#Giving alias name  import module as alias_name

# or from math import method as alias_name


import math as m
#print(m.sqrt(9))


from math import pi,sqrt as sq

#print(pi)
#print(sq(9))
