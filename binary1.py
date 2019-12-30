def binary_search(lst, left, right, elem):
	mid = (left+right)//2
	
	if lst[mid] == elem:
		return True
	elif lst[mid] > elem:
		right = mid
	elif lst[mid] < elem:
		left = mid
	
	if abs(right-left) < 2:
		return False

	return binary_search(lst,left,right,elem)

