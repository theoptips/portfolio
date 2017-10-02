# hueristic
# number checking website - http://www.numberempire.com/10110133
# 	https://primes.utm.edu/nthprime/index.php#random
# realistically need to check if divisible by any known prime number
# small_known_prime = [1,2,3,5,7,11,13,17]
# for x in small_known_prime: x % 2 == 1 except for 1, 9 is falsely returned as prime
# if a natural number is not prime, then it is called composite number

# first iteration
def is_prime_1(x):
	if x > 1:
		iteration = x // 2 # floor
		for i in range (2, iteration + 1):
			if x % i == 0:
				return False
		return True
	else:
		return False

def test(prime_candidate, expected_result):
	c = prime_candidate
	r = expected_result
	if (is_prime_1(c) and r) or (is_prime_1(c) == False and r == False):
		print "test for" + str(c) + "is correct!"
	else:
		print "test for" + str(c) + "Failed"

test(1011013, True)
test(88, False)
test(10110133, False)
test(1, True)

# while there are ways to save time, such as take 9 out of the iteration, but it is also very convenient to just 
# go through the potential candidates in order
# if we check for all known primes, it is quite recursive, big O gets big

# interesting facts about prime
# prime number can be used in public key crypto

