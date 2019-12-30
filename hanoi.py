def han(d,f,t,i):
	if d==1:
		return (f+"->"+t+"\n")
	else: 
		return han(d-1,f,i,t)+(f+"->"+t+"\n")+han(d-1,i,t,f)
d=int(input("Type number of disks:"))
print(han(d,"start","destination","via"))
