nums = [1,2,3,4,5]
new_list = [n for n in nums]
print new_list

new_list = [n*n for n in nums]
print new_list

new_list = map(lambda n: n*n, nums)
print new_list
