def countPrimes(n):
    counter = 0
    def isPrime(n):
    
        for i in range(2,n):
            if n % i == 0:
                return False
                
        return True

    """
    :type n: int
    :rtype: int
    """
    for i in range(2,n): #n+1 if include self
        if isPrime(i):
         counter += 1
        
    return counter 



    print str(isPrime(17)) + "-> True"
    print str(isPrime(14)) + "-> False"
    print str(isPrime(9))  + "-> False"
    print str(isPrime(23)) + "-> True"
    print str(isPrime(179)) + "-> True"
    print str(isPrime(177)) + "-> False"
    print str(isPrime(178)) + "-> False"
    print str(isPrime(4)) + "-> False"
    




    
#print countPrimes(3) #2 -1
#print countPrimes(8) #4 -1
#print countPrimes(7) #4 -1
print countPrimes(1000) #168 -1
#print countPrimes(4) #2 -1
#print countPrimes(2) #2 -1