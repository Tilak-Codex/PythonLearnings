#String methods

#1.capitalize(string)---> Converts the char in 0th index to uppercase and ensures that the remaining characters are in lowercase

str1="hello I am from India"   #len ---> 21

#print("capitalize() "+str1.capitalize())


#2.lower(string) ----> converts all the characters to lowercase.
#3.casefold(string) ---> similar to lower() but more aggresive(converts even unicodes).
str2="casefold ß and lower"
#print("casefold() "+str2.casefold())
#print("lower() "+str2.lower())

#4.center(length,"character_used_in_alignment") ---> Used to centre alignto string
"""how it actually works ---> if the length parameter is grater than the length of string object then the string is centered
      if the length parameter is less than or equal to the length of the string than noting happens
      it adds the given character in the squence first in right next in left then again in right and so on"""
#print("center() "+str1.center(30,"#"))

#5.count(char) ---> returns the total number occurence of a character inthe given string.
#print(str1.count('i'))

#6.encode("encoding_format-utf-8,ascii",erroes="strict")---> encodes a string into specific format,such as utf-8 or ascii
""" The ouput will will have b'str' which indicates that the data is represented as bytes rather than
        string so b represents the byte objectcontaing the enocded version of str"""
#print("©".encode("ascii",errors="backslashreplace"))
""" errors = "strict" is default to handle the error that ist raises UnicodeEncodeError
       The values can be "ignore","replace","xmlcharrefplace","backslashreplace"""
"""
strict ---> rasies default error UnicodeEncodeError
ignore  ---> ignores charaters that cannot be encoded
replace ---> replaces characters that that cannot be encoded using ?(replacement character)
xmlcharrefreplace--->replaceswith XML numeric character reference
backslashreplace ---> replaces wit backslash"""
#REMARK ---> LEARN ABOUT VARIOUS ENCODING FORMATS FOR BETTER UNDERSTADING

#7.endswith("substring",[start],[stop])--->checks whether the given string ends
#returns either True or False
#print(str1.endswith("ia"))


#8.expandtabs(size)---> replaces tabs in string with spaces
""" if size not given it assumes tab size of 8
       Tab is replaced by 4 spaces(of size 1)"""
str3="hello\tworld"  #len = 11
#print("We are leanring expandtabs()method")
#print(len(str3))
s=str3.expandtabs(5)
#print(len(s))
#print(s)
"""
        This was quite hard... so we need to understand about tab stops
        Tab stops ---> Tab stops are simply multiple of 8.
        The number of white spaces added is determined by its position.
        If the /t is in position(index) 3  so tab stop value is 8 & (8-3) is 5 so 5 spaces are added.
        if the /t postion is 9 than tabstop value is 16.
        if you set size to 2 then tab stops are 2,4,6,8 etc...
"""
#9.find(sub,[start],[end]) ---> returns the index of first occurence of given sub string,if not found returns -1
s="hello help me to find i"
#print(s.find("i"))
#print(s.index("i"))

#10.format
#11.format_map()

#12.index(sub,[start],[end]) ---> returns the first occurence of given substring ,
"""if sub is not found valueError is raised"""
#print(s.index("h"))

#Now starting with is methods, there are 12 is methods in python
"""13.isalnum(), 14.isalpha() , 15.isascii(), 16.isdecimal,17.isdigit() 18.isidentifier(),
      19.islower(),20.isnumeric(), 21.isprintable(), 22.isspace(), 23.istitle(), 24.isupper()
"""

#25sep.join(iteratable)---> joins the elements of an iteratable using given separator.
"""Note - The iteratablemust contain only string elements."""
l=['1','2','3','4']
t='1','2','3','4'
s="hello"
d={'1':"h","2":"e","3":"l"}

#print("Join with list "+"#".join(l))
#print("Join with tuple "+"#".join(t))
#print("Join with string "+"#".join(s))
#print("Join with dictionary "+"#".join(d))   #Keys only joined

#26.ljust(with,[fillchar])               if width is smaller than len chars added to  the right until  
s="hello world"   #len = 11
#print(s.ljust(15,"*"))

#27.lower() ---> converts all chars ina string to lowercase.
#28.lstrip([chars]) ---> removes given char from left , until first mismatch.
'''IF char is not given whitespace is removed'''
s='HIhiHellohihello'
#print(s.lstrip("HIi"))

#29.rstrip([chars]) ---> similar to lstrip() but works from right
#print(s.rstrip("HIhiHellohihello"))

#30.strip([chars])---> removes both leading and trailing chars.it is cares about mismatch
s="xoxo loxve xoxo"
#print(s.strip("xoe"))





