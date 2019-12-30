def ck(l):
	if type(l) is list:
		if len(l)>=3:
			op=l[-1]
			if op in ["+","-","*","/"]:
				result =True
				for i in l[:-1]:
					if type(i) is not int:
						result =result and ck(i)
				return result
			else:
				print("no")
				return False
		else:
			print("no")
			return False
	else:
		print("no")
		return False
l=[3,[6,2,"/"],"*"]
print(i)
