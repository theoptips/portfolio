# def isPrime(n):
#     factor = n
#     counter = 0
#     while factor > 1:
#         if n % factor == 0:
#             counter += 1
#         factor -= 1

#     if counter == 1:
#         return True
#     else:
#         return False    


#better implementation
#can only be divisible by 1 and itself
#no need for counter 
#each item itself is a flag
#no need to check 1 and self, always divisble if int
def isPrime(n):
    for i in range(2,n): #caution n other than itself hence excluded
        if n % i == 0:
            return False
    return True
#O(n)

print str(isPrime(17)) + "-> True"
print str(isPrime(14)) + "-> False"
print str(isPrime(9))  + "-> False"
print str(isPrime(23)) + "-> True"
print str(isPrime(179)) + "-> True"
print str(isPrime(177)) + "-> False"
print str(isPrime(178)) + "-> False"
print str(isPrime(4)) + "-> False"


# def countPrime(n):
#     factor = n
#     counter = 0
#     # excluding 1
#     while factor > 1:
#         if isPrime(factor):
#             counter += 1
#         factor -=1
#     return 

# better countPrime(n)
#inplace
#must include self
#O(n^2)
def countPrime(n):
    counter = 0
    for i in range(2,n+1): #caution! n+1 if self counts, n if does not
        if isPrime(i):
            counter += 1
    return counter 




print countPrime(3) #2
print countPrime(8) #4
print countPrime(7) #4
print countPrime(1000) #168
print countPrime(4) #2
print countPrime(2) #2





