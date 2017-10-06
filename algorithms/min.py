def find_min(array):
	min = array[0] #set 1st element as min placeholder
	for i in array:
		if i < min:
			min  = i
	return min

print(str(-5))
print(find_min([-1,3,4,13,2,0.5,-5]))

print(str(0.5))
print(find_min([3,4,13,2,0.5]))
print(str(2))
print(find_min([3,4,13,2]))
	
