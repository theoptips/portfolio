#sieve of eratosthenes first 100
import numpy as np
l = [i for i in range(2,101)]
# intuition for square root, just have to check the first 9or10 digits
base = np.sqrt(len(l))

for i in range(2, int(base)):
	#print(i)
	l = filter(lambda x : x % i != 0 and x!=i, l)

print(l)
