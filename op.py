def eval(x):
    if type(x) is list:
        op=x[-1]
        if op =="+":
            sum=0
            for i in x[:-1]:
                sum+=eval(i)
        elif op=="-":
            res=eval(x[0])
            for i in x[1:-1]:
                res-=eval(i)
        elif op=="/":
            mi=eval(x[0])
            for i in x[1:-1]:
                mi/=eval(i)
        elif op=="*":
            re=1
            for i in x[:-1]:
                re=re*eval(i)
    else:
        return x
x=[3,[6,2,"/"],"*"]
print(x)
print(eval(x))

