#1.append(item) ---> Adds the given item at the end of the list
'''It returns None'''
l=[1,2,3,4]
l.append(5)
#print(l)

#Adding sequence

l.append([1,2,3])
l.append((1,2,3))
l.append("hello")
#print(l)

#2.insert(index,item) ---> Adds the given item at the given index(similar to append)
"""It returns None"""
l1=[1,2,3]
l1.insert(1,5)
#print(l1)

#Adding sequence
l1.insert(1,(1,2,3))
#print(l1)

#3.extend(iterable) --->Adds items of an iterable at the end of the list
"""It returns None"""
l2=[1,2,3]
"""l2.extend(2)""" #This gives type error
l2.extend([1,2,3])
#print(l2)

#4.copy()  ---> Retruns deep copy of the list
"""Returns a list"""
"""Deep copy ---> changes done in original list will not affect the duplicte list and vise versa"""   #deep ->Independent
l3=[1,2,3]
l4=l3.copy()
l3.append(5)
#print("l3",l3)
#print("l4",l4)
#print(id(l3))
#print(id(l4))
"""IDs are different"""
#List copy using =  (It does shallow copy)
l3=[1,2,3]
l4=l3
l4.append(5)
#print("l3",l3)
#print("l4",l4)
#print(id(l3))
#print(id(l4))
"""IDs are same"""
#List copying using slicing --->Deepcopy
l3=[1,2,3]
l4=l3[:]
#print("l3",l3)
#print("l4",l4)
#print(id(l3))
#print(id(l4))

#5.clear() ---> Removes all the items from the list leaving behind empty list
""" Returns None"""
l5=[1,2,3]
l5.clear()
#print(l5)

#6.pop(index) --->removes element at given index (if no index is given last element is removed)
""" Returns the removes item"""
l3=[1,2,3,4,5]
#print(l3.pop(4))
#print(l3)

#7.remove(item) --- Removes the element from its first occurence
"""It returns None"""  """If given element is not present it raises ValueError"""
l3=[1,2,3]
l3.remove(3)
#print(l3)

#8.count(item) ---> returns the totaloccurence of given item
""" retuens integer"""
l3=[1,2,1,3,4]
#print(l3.count(1))

#9.index(item,[start],[stop]) ---> returns the index of first occurence of given item
""" Returns integer"""
l3=[1,1,1,2]
#print(l3.index(1))

#10.reverse() --->reverses the order of elements in a list
""" Returns None"""
l3.reverse()
#print(l3)

#11.sort(reverse=True/False,key) ---> Arranges list in ascending or descending order

"""
        It returns None
        By defalut reverse is False so the list is sorted in ascending order
        if reverse is True the list is sorted in decensing order
"""

l6=[1,4,2,6,74,0]
l6.sort()
print(l6)
l6.sort(reverse=True)
print(l6)
