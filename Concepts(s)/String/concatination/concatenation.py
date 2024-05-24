var1="hello"
var2="world"
#1.using + operator
var3=var1+var2
#print(var)

#2.using str.join(iteratable)    the iteratble must contain only string elements

"""join() method returns a string by joining two strings using a separator"""

var4="".join([var1,var2])   #or "".join((var1,var2))
#print(var4)
var4="".join((var1,var2))
#print(var4)

#3.using % operator
print("%s%s"%(var1,var2))
#4.using forma()

print("{}{}".format(var1,var2))

#5.Using fstring 
print(f"hello var1 {var1} and var2 {var2}")



