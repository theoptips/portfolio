wdef relu(twod_array):
	arr = twod_array
	m = len(twod_array)
	for i in range(0,m):
		n = len(arr[i])
		
		for j in range(0,n):
			if arr[i][j] < 0:
				arr[i][j]=0
	return arr

print relu([[2,-1],[1,-1,-5]])
				  
def relu_2(twod_array):
	arr = twod_array
	n = len(arr)
	for i in range(0,n):
		m = len(arr[i])
		for j in range(0,m):
			arr[i][j] = max(arr[i][j], 0)
	return arr			

print relu_2([[2,-1],[1,-1,-5]])

