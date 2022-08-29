
# n=int(input("enter no"))
def fun(n):
    i=0
    b=[]
    while i<=n:
        m=2**i
        b.append(m)
        print(2,"^",i,"=",b)
        i+=1
fun(2)