#twosum



def TwoSum(l,num):
    for i in range(len(l)):
        for j in range(1,len(l)):
            if l[i]+l[j]==num:
                return i,j



print(TwoSum([3,2,4],6))
