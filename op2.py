def eval(x):
	if type(x) is list:
		op=x[-1]
		if op =="+":
			res=0
			for i in x[:-1]:
				res+=eval(i)
		elif op=="-":
			res=eval(x[0])
			for i in x[1:-1]:
				res-=eval(i)
		elif op=="/":
			res=eval(x[0])
			for i in x[1:-1]:
				res=res/eval(i)
		elif op=="*":
			res=1
			for i in x[:-1]:
				res=res*eval(i)
	else:
        return x
        
def check(l):
            if type(l) is list:
                if len(l)>=3:
                    op=l[-1]
                    if op in ["+","-","*","/"]:
                        res=True
                        for j in l[:-1]:
                            if type(j) is not int:
                                res=res and check(j)
                        return res
                    else:
                        print("Nah")
                        print(l)
                        return False
                else:
                    print("NO")
                    print(l)
                    return False
            else:
                print("nonon")
                print(l)
                return False
l=[3,[6,2,"/"],"*"]
if not check(l):
    print("dang")
print(l)
print(eval(l))

           
x=input("type yuor op:")

