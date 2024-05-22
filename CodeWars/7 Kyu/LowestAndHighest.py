#Highest and lowest

#in a string of numbers separated by space find lowets and highest number


def func(numbers):
    l2=[int(i) for i in numbers.split()]
   #print(l2)
    x,y=str(max(l2)),str(min(l2))
    z="{} {}".format(x,y)
    return(z)

print(func("-9 12 1 100"))
    
  
