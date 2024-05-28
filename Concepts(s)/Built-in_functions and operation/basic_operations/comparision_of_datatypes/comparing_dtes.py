                                                                #Comparing operation in python

                    
#For knowing about data types in pyton please refer to image DATA_TYPES in the parent folder.

""" For comparing the data types we use relational operators such as

                        ==
                        !=
                        <
                        <=
                        >
                        >=
"""

#Comparing Integers are just cake walk
#Comparing Bool is also very easy just remember True=1 and False=0

#Comparing sequence

#1.String

"""Using Equality operation   ---> For strings to be equal they need to be exactly same"""
s1="hi"
s2="hi"
#print("s1=s2?",s1==s2)

""" Using greater etc---> for these kind of opearation, ascii value is used irrespective of their length"""
s1="hello"
s2="aorld"
#print(s1<s2)

#2.List

"""Using Equality operation ---> Both the list must be exactly same"""
l1=[6,2,3]
l2=[5,2,3,4]
#print(l1==l2)

"""Using greater etc ---> Compares each and every element of both the list, the list with first greater element is larger"""
#print(l1<l2)

#3.tuple
t1=(4,2,3)
t2=(1,2,3,4)
#print(t1<t2)

"""Using greater etc ---> Compares each and every element of bot the tuple, the tuple with first greater element is larger"""

#Mapping(Dictionary)
"""Two dictionariesare equal only if both the key and values are exactly the same"""
"""It does not support <,<=,>,>="""
#Sets
"""   == (Equality)         --> Two sets are  exactly same.
        != (Inequality)       --> Sets which are not exactly same.
        <= (Subset)           --> Every element in A is present in B ( B can contain more elements)
        < (proper subset)  --> A is proper subset of B if , B contains atleast one element that is not present in A.  aka Strict subset
        >= (Superset)        --> A contains all elements of B and contains additional element also.
        >(proper superset)--> 
"""
s1={1,2,3}
s2={1,2,3,4}
#print(s1==s2)
#print(s2>s1)



