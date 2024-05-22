                                                                #LIST COMPREHENSION
""" List comprehension offers a concise way to create a new list from the values an existing list """

#syntax -->  [expression for item in list [if condition ==True]


#To create a list whose values are square of values in an existing list

numbers=[2,3,4,5]

sq_numbers=[num ** 2 for num in numbers]

print(sq_numbers)


#square only when num is odd


sq_numbers=[num ** 2 for num in numbers if (num%2!=0)]

print(sq_numbers)

""" THE VALUES WHICH SATISFY THE CONDITION IS EVALUATED USING THE EXPRESSION AND THE RESULT IS STORED IN THE NEWLIST"""
