                                        #Tuple packing & unpacking

a=(1,2,3,4)   #this is packing
#UNPACKING
""" Assigning values of tuple to variables"""
""" Number of variables must e equal to number ofelemetns in the tuple"""
w,x,y,z=a
#print(w)
#print(x)
#print(y)
#print(z)

#UNPACKING using Asterisk
"""If the no.of variables is less we can use asterisk
     put * infront of variable name
     the var stores remaining values as a list"""

t=("banana","apple","cabbage","watermelon","cucumber")
yellow,*red,green=t
#print(yellow)
#print(red)
#print(green)

#UNPACKING using underscore
"""instead using name, wecan simply useunderscore"""
w,x,y,_=a
#print(w)
#print(x)
#print(y)
#print(_)
