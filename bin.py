def binsearch(L,s):
    k=len(L)//2
    if L[k]==s:
        return True
    elif L[k]>s:
        return binsearch(L[:k],s)
    else:
        return binsearch(L[k+1:],s)
L=[]
s=input("Type the letter you want to find:")
print(binsearch(L,s))



		