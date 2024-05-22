#vowel count
"""
def get_count(sentence):
    count=0
    for i in sentence:
        if i.lower() in "aeiou":
            count+=1
        else:
            continue
    return count


print(get_count(input("Enter")))

"""
#Best solution

def get_count(sentence):
    return sum(1 for i in sentence.lower() if i in "aeiou")

print(get_count("Hello"))
