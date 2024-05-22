#Find the int that occurs odd number of times

def OddInt(l):
    for i in l:
        if l.count(i)%2!=0:
            return(i)

z=OddInt([2,2,3,4,2,3,4,2,3])
print(z)
