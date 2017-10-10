#sieve of eratosthenes
hard = [1]
digits = [i for i in range (0,10)]
base = [2,3,5,7]
l = [i for i in range(6,101)] #first 100 numbers, starting with first composite number
#l3 = filter(lambda x: x%3 !=0, l2)
#An algorithm yielding all primes up to a given limit, such as required in the primes-only trial division method, is called a prime number sieve.

for i in base:
	l = filter(lambda x : x % i != 0, l)

new_base = []
for i in l:
	new_base.append(i)
	l = filter(lambda x : x % i != 0, l)


prime = hard + base + new_base
print(prime)