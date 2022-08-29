#doc.q5
def fun():
    List = [1,2,3,3,3,3,4,5]
    i=0
    b=[]
    while i < len(List):
       if List[i] not in b:
          b.append (List[i])
       i=i+1
    print(b)
fun()
