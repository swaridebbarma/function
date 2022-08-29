#doc.q45
def fun():
    i=0
    while i<=10:
        n=int(input("enter no :"))
        if n%2==0:
            a=n*100
            print("even no:",a)
        else:
            b=n*(-1)
            print("odd:",b)
        i+=1
fun()