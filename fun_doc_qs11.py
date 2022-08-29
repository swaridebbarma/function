#doc.q11
def generateRange(min,max,step):
    i=min
    a=[]
    while i<=max:
        if step>0:
            a.append(i)
            i+=step
    print(a)
generateRange(2,10,2)
generateRange(1, 10, 3) # should return list of [1,4,7,10]


