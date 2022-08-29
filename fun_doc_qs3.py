# #doc.q3
# def fun(num): 
#    sum=0
#    for i in num:
#       sum+=i
#    return sum
# print(fun((8,2,3,0,7)))


def fun(n):
   i=0
   s=0
   while i<len(n):
      s=s+n[i]
      i=i+1
   print(s)
n=[8,2,3,0,7]
fun(n)
   