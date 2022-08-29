# def list_change():
#     l=([5, 10, 50, 20], [2, 20, 3,5])
#     multi=1
   #  multi1=1
#     multi2=1
#     new_list=[]
#     i=0
#     while i<len(l):
#       j=0
#       while j<len(l[i]):
#          if j==0:
#             multi*=l[i][j]
#          elif j==1:
#             multi1*=l[i][j]
#          elif j==2:
#             multi2*=l[i][j]
#          j+=1
#       i+=1
#     new_list.append(multi)
#     new_list.append(multi1)
#     new_list.append(multi2)
#     print(new_list)
# list_change()





#meraki.q18
def list_change():
   a=[5, 10, 50, 20]
   b=[2, 20, 3, 5]
   i=0
   new_list=[]
   while i<len(a):
      while i<len(b):
         m=a[i]*b[i]
         new_list.append(m)
         i+=1
   print(new_list)
list_change()
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
