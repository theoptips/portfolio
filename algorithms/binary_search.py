#popular practice
#mid+1
#mid-1
#return -1 if not found
#recursively use binary search

def binary_search(sorted_array,item):
	list = sorted_array
	low = 0 
	high = len(list) - 1
	
	while low <= high:
		mid = (low + high) /2 #python rounds down automatically if not even
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

list = [1,3,4,5,7,9,10]

print binary_search(list, 3) # => 1
print binary_search(list, -1) # => None
print binary_search(list, 22) # => None
print binary_search(list, 5) # => 3
