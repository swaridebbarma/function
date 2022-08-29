#doc.q8
def fun():
    a='The quick Brow Fox'
    i=0
    c=0
    c1=0
    while i< len(a):
        if a[i]>= "a" and a[i]<= "z":
            c+=1
        if a[i]>= "A" and a[i]<="Z":
            c1+=1
        i+=1
    print("No. of Uppercase characters :-",c)
    print("No. of Lower case Characters :-",c1)
fun()
