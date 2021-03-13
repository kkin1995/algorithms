
def linearSearch(list,element):
	for i in storage:
		if element == i:
			return True
	return False

def binarysearch(list,element):
	sorted_list = sorted(list,key=int)
	left = 0
	right = len(sorted_list) - 1
	while left <= right:
		mid = (left + right) // 2
		if element == sorted_list[mid]:
			return True
		elif element < sorted_list[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return False

print(binarysearch([2,4,9,5,3],3))