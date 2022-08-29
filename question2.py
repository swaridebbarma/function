#Q2
def perfect():
    i=1
    while i<1000:
        b=i
        j=1
        sum=0
        while j<i:
            if b%j==0:
                sum+=j
            j+=1
        if sum==b:
            print(j,":perfect number")
        i+=1
perfect()