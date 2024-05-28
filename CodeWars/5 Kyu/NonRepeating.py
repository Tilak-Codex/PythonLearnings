#To take a string as input and return first non repeating character from it...

def FirstNonRepeating(s):
    s1=s.lower()
    for i in s1:
        if (s1.count(i)==1):
            return i
    else:
        return ''
z=FirstNonRepeating("hIHello")
print(z)
