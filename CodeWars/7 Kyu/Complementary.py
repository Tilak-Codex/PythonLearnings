#Complementary of T with A and G with C
'''
def Comp(s):
     s1=""
     for i in s:
        if i=="T":
            s1+="A"
        elif i=="A":
            s1+="T"
        elif i=="G":
            s1+="C"
        elif i=="C":
            s1+="G"

     return s1


print(Comp("TTAGCA"))
'''

#MISTAKES
# 1. If you use replace method it will replace the char with given char at once

#CLEVER

pairs={'A':'T','T':'A','G':'C','C':'G'}

def dna(st):
    return(''.join(pairs[x] for x in st))


print(dna("TTAGCA"))
