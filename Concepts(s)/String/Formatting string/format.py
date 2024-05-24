#format
"""
        Format() consists of curly braces as placeholders
        value can be string,int,float or var
"""

#Default order

s="{}{}{}".format('i','am',' learning')
#print(s)


#positional formatting

s="{1}{0}{2}".format('i','am','learning')
#print(s)


#Keyword formatting

s="{c}{b}{a}".format(a='i',b='am',c='learning')
#print(s)

#Represent numbers in their other types

s=16

#print("The binary representation of 16 is:{:b}".format(16))
#print("The hexadecimal representation of 16 is {0:x}".format(16))

#Alignment
"""
        :<n - left alignment
        :>n - right alignment
        :^n - center alignment
"""


print("Left alingment{:>10}".format("Hello"))
