# 0 n=0
# 1 n=1
# fn-1 + fn-2 if n>1

# 0 1 1 2 3 5 8 13 21

def f(n):
	if n == 0:
		return 0
	elif n == 1: 
		return 1
	else: 
		return f(n-1) + f(n-2)

result = [f(3)]
print(result)