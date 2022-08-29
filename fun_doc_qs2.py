def fun ():
      n=[2,5,7,8,3,6,9,4]
      i=0
      m=0
      sm=0
      thm=0
      while i<len(n):
        if n[i]>m:
            m=n[i]
        i=i+1
      sm=0
      i=0
      while i<len(n):
        if n[i]<m and n[i]>sm:
              sm=n[i]
        i=i+1
      thm=0
      i=0
      while i<len(n):
        if n[i]<sm and n[i]>thm:
            thm=n[i]
        i+=1
      print(m,sm,thm)
fun()





       