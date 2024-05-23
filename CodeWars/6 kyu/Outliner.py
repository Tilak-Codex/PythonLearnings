#OUTLINER

"""
    The list may contain complelty odd or even numbers except one number.
    find odd number from the list
    list may contain 3or more elelemts.

"""
#Solution

"""
        The list will contain 3 elements for sure
        if there are two even numbers then it must be a even array in which we have to find the odd number
        Vice versa
"""
"""
def Outliner(l):
    count_even=0
    count_odd=0
    for i in l[0:3]:
        if i%2==0:
            count_even+=1
        else:
            count_odd+=1
    if count_even>1:
        for i in l:
            if i%2!=0:
                return i
    if count_odd>1:
        for i in l:
            if i%2==0:
                return i
print(Outliner([2,3,5,7,9]))
"""

#Clever
def Outliner(int):
    odds=[x for x in int if x%2!=0]
    evens=[x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

print(Outliner([2,3,5,7,9]))
