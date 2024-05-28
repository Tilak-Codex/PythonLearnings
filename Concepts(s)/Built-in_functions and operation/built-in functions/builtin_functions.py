                                                            
                                                        
                                                                #Built-in functions in python
#1.abs(item) ---> Returns absolute value of given item
""" i/p = number(integer,float,complex)
      Absolute value -> |value|
      |comple.no| = sqrt(x2+y2)
"""
#print("abs-int",abs(5))  
#print("abs-int(-ve)",abs(-5.0))
#print("abs-float",abs(5.3))
#print("abs-comple",abs(5+1j))

#2.all(iterable) --> Returns true if all the elements of the iterable are True
l=[1,2,3]
#print(all(l))
#use case -> In checking multiple conditions and all has to be true
#eg
#In dictionary, only keys are considered
likes=1200
comm=500
k=[likes>1000,comm>300]
"""if all(k):
    print("awesome video")"""


#3.any(iterable) ->Returns true if anyone condition in the iterable is true
l=[1,2,3]
#print(any(l))
#use case -> In checking multiple conditions and all has to be true
#eg

likes=1200
comm=200
k=[likes>1000,comm>300]
#if any(k):
#    print("awesome video")

#4.callable(object) -> Returns True if the given object is callable else false
""" Even if callable() returns True the funtion may be unable to call
      But if it returns False we cannot call the object certainly"""
#print(callable(str.count()))

#5.min(seq) -> Returns minimum value in a sequence

#6.max(seq) -> Returns maximum value in a sequence
