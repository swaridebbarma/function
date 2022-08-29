#doc.q4
def fun():
    a="1234abcd"
    i=-1
    while i<len(a):
        b=(a[i::-1])
        i+=1
    print(b)
fun()
 



