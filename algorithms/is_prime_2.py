def isPrime(n):
    factor = n
    counter = 0
    while factor > 1:
        if n % factor == 0:
            counter += 1
        factor -= 1

    if counter == 1:
        return True
    else:
        return False    

print str(isPrime(17)) + "-> True"
print str(isPrime(14)) + "-> False"
print str(isPrime(9))  + "-> False"
print str(isPrime(23)) + "-> True"
print str(isPrime(179)) + "-> True"
print str(isPrime(177)) + "-> False"
print str(isPrime(178)) + "-> False"


def countPrime(n):
    factor = n
    counter = 0
    # excluding 1
    while factor > 1:
        if isPrime(factor):
            counter += 1
        factor -=1
    return counter

print countPrime(3) #2
print countPrime(8) #4
print countPrime(7) #4
print countPrime(1000) #168
