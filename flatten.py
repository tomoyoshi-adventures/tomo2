L=[]
def flatten(S,flat):
	if S==[]:
		return
	for x in S:
		if isinstance (x,list):
			flatten(x,flat)
		else:
			flat.append(x)
        flatten(S,L)
print(L)
		