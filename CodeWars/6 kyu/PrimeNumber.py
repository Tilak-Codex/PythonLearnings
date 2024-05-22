#A number is primeor not


def CheckPrime(n):
       
        for i in range(2,n):
                if n % i==0:
                    return False
        return True

print(CheckPrime(-23))
