                                                                              #Assert keyword
#syntax

"""
            assert exp, statemet
if the exp is true the statement does nothing if false returns the statement as an exception

"""

def age(value):
    assert value >0 and value <100 ,"Please enter a valid age you dummy....!"
    print(value)

age(int(input("Enter your age")))




#If the given exp is evaluatedto be False AssertionErroris raised with given statement
