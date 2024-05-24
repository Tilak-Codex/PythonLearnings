                                                                            #Dictionary Methods
#1.clear() -> Removes all itemsfrom dict .  Does not return anything.

#2.copy() -> Returns a shallow copy(does not modify the original dict) of  the dictionary.

#3.fromkeys(key,value)-> creates a dictionary from the given sequence of keys and values.
"""Note that we are calling the method using dict class object"""
keys={1,2,3}
values={'a','b','c'}
#print(dict.fromkeys(keys,values))

#4.get(key,[value]) -> Returns value of given key, if key is not present given value arg is retunded
d1={1:'a',2:'b',3:'c'}
#print(d1.get(1))
#print(d1.get(5,"not found"))
""" D/b get() and dict[key]
get() returns defauly value when key is not found but dict[key] raises KeyError
if default value is not given it returns None
"""

#5.items() -> returns a view object(called dict_items()) that displays a list of dict keys and values in tuple pair.
#print(d1.items())
"""View objects are such objects which refreshes dynamically whenever any change occurs in the contents of their source dict."""

#6.keys() -> returns a view object(named dict_keys())that displays a list of all the keys present in the dict.
#print(d1.keys())

#7.pop(key,[default]) ->removes the element in the given key and returns the value.(default value is returned when key not found).
"""If key is not found amd default value is not specified KeyError is raised."""
#print(d1.pop(1,"no such key"))

#8.popitem() -> Removes and returns last (key,value) pair in tuple (works in LIFO order)
"""Raises key error when dict is empty."""
#print(d1.popitem())

#9.setdefault(key,[default_value]) -> inserts valu if given key is not present in the dict.
"""key ->Key to be searched in the dict
     default_value --> key value pair to be inserted  into the dictionary when given key is not found
     if default value is not given None is its value
"""
"""
    Returns value of the key if it is present.
    None if key is not present in the dict and default_value is not  specified
    Returns default_value ig given key is not present in te dict.
"""
#print(d1.setdefault(3))
#print(d1.setdefault(4,(1,2)))
#print(d1)

#10.update() -> this method updates the element of one dictionary withother
""" d1.update(d2) -> values are d1 are updated using d2
       It returns None"""

#11.values() -> Returns a view object(called  dict_values() which contains all the values present in a dict in a list

