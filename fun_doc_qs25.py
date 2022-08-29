#doc.q25
list1 = [2, -7 ,45, -64, -14]
def fun(list1):
    i=0
    c1=0
    c2=0
    while i<len(list1):
        if list1[i]>0:
            c1+=1
        else:
            c2=c2+1
        i=i+1
    print(c1,"positive number")
    print(c2,"is negative number")
fun(list1)