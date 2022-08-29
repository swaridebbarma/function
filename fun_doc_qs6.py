#doc.q6
def fun(List):
   i=0
   b=[]
   while i<len(List):
       if List[i]%2==0:
           b.append(List[i])
       i+=1
   print(b)
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fun(List)