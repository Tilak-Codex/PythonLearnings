#removing vowels froma string

"""
def disemvowel(s1):
    s2=""
    for i in s1:
        if i in "aeiouAEIOU":
            pass
        else:
            s2+=i
    return s2


print(disemvowel("This website is useless"))
"""
#CLEVER


def remove(s):
    return "".join(c for c in s if c.lower() not in "aeiou")


print(remove("This website is useless"))
