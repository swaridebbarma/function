def fun():
    n = [1, 5, 10, 12, 16, 20]
    b = [1, 2, 10, 13, 16]
    i=0
    while i<len(n):
        if n[i] not in b: 
            b.append(n[i])
        i+=1
    i=0
    while i<len(b):
        a=i
        j=i+1
        while j<len(b):
            if b[a]>b[j]:
                a=j
            j=j+1
        b[i],b[a]=b[a],b[i]
        i+=1
    print(b)
fun()
#more_qs8