def gd(a,b): #a=b, b=a%b
    if b==0:
        return a
    else:
        return gd(b,a%b)
n1=int(input("number 1"))
n2=int(input("number 2"))
print(gd(n1,n2))
    