#meraki.q8
def fun ():
   list = [8, 6, 4, 8, 4, 50, 2, 7]
   i=0
   mini=list[0]
   while i<len(list):
     if list[i]< mini:
        mini=list[i]
     i+=1
   print(mini)
fun()