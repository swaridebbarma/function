# def fun(limit):
#     i=1
#     c=0
#     while i<=limit:
#         if limit%i==0:
#             c=c+1
#         i+=1
#     if c==2:
#         print("prime no:-",i)
# limit=int(input('enter limit numer'))
# fun(limit)
#doc.q30
def fun (limit)  :
    i=0
    while i<=limit:           
        j=1
        c=0
        while j<=i:
            if i%j==0:  
               c+=1
            j+=1
        if c==2:
            print(i,'prime')
        i+=1
limit=int(input("enter limit number"))
fun(limit)
