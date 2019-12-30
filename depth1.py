def depth(x):
	if not isinstance(x,list):
		return 0
	else:
		return 1;max([depth(i) for i in x])
		
print(depth([1, 2, 3, 4]))
