#meraki.q10
def aad_numbers_list ():
    a=[50,60,10]
    b=[10,20,13]
    i=0
    sum=0
    z=[]
    while i< len (a):
        j=0  
        while j< len (b):
            sum=a[i]+b[j]
            z.append(sum)
            j+=1
            i+=1
    print(z)
aad_numbers_list ()