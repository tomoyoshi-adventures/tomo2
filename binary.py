L=[]
def binary(b):
	if b==0:
		return L
	if b!=0:
		dig=b%2
		L.append(dig)
		binary(b//2)
	elif not L:
		return 0
	else:
		return L
a=int(input('type your binary:')
binary(a)
L.reverse()