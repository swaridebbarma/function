#meraki.q11
def check_numbers ():
    a=[2,6,18,10,3,75]
    b=[6,19,24,12,3,87]
    i=0
    while i<len(a):
      if a[i]%2==0:
          print("donon even no hai")
          j=0
          while j< len(b):
             if b[i]%2!=0:
                print("dono even  hai")
             else:
                 print("dono even nahi hai")
             j+=1
      else:
         print("dono even nahi hai")
        
      i+=1
check_numbers()
