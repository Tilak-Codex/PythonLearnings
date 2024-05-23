#Simple pig latin

"""
        In each word of string move the first letter to last and add ay avoid puncuation marks
"""

def PigLatin(s):
    s1=''
    l=s.split()
    for i in l:
        if i.isalpha():
            s1+=i[1:len(i)+1]+i[0]+"ay "
        else:
            s1+="!"
    print(s1)



PigLatin("Pig latin ")
    
