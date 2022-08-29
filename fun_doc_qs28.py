#doc.q28
def showNumber(limit):
    i=0
    while i<=limit:
       if i%2==0:
           print(i,'even')
       else:
           print(i,'odd')
       i=i+1
showNumber(3)