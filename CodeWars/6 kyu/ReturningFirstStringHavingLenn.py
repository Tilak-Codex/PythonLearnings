#Returning first string having n consecutive strings
from string import ascii_lowercase
def longest_Conse(str,k):
    n=len(str)
    if n==0 or k>n or k<=0:
        return  None
    for i in str:
        if len(i) == k:
            if i.lower() in ascii_lowercase:
                return i
    return "".join(str)

print(longest_Conse("This is a aaa aa abc de efgh ijk lmnop".split() ,10))
