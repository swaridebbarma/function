#doc.q41
num=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
def check(num):
    i=0
    max=0
    while i < len(num):
        j=0
        c=0
        b=[]
        while j<len(num[i]):
            if (num[i][j])>max:
                max=num[i][j]  
                b.append(max)
                c=c+1
            j+=1
        i+=1
    print((c,b))
    i=0
    mini=num[0]
    c=1
    while i< len(num):
        if num[i]<mini:
            mini=num[i]
            c+=1
        i+=1
    print((c,mini))
check(num)
        
        