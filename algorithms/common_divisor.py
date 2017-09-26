def greatest_common_divisor(first_num, sec_num, iteration=0):
	if first_num == sec_num:
		result = first_num
		print "result is", first_num
		return result
	elif first_num == 0:
		if iteration == 0:
			print "result is", sec_num
			return sec_num
		else:
			print "result is 1"
			return 1
	elif sec_num ==0:
		if iteration == 0:
			print "result is", first_num
			return first_num
		else:
			print "result is 1"
			return 1

	if first_num > sec_num:
		first_num = first_num - sec_num
	elif first_num < sec_num:
		sec_num = sec_num-first_num
	
	iteration = iteration + 1
	print first_num, sec_num
	greatest_common_divisor(first_num, sec_num, iteration)


		
print(greatest_common_divisor(80,60))
print(greatest_common_divisor(5,7))
print(greatest_common_divisor(0,99
))
print(greatest_common_divisor(98,0
))
print(greatest_common_divisor(13,1287))
print(greatest_common_divisor(54,24))