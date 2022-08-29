#doc.14
def fun () :   
     i=1
     c=0
     while i<=num:
        if num % i ==0:
           c=c+1
        i+=1
     if c==2:
       print('prime no')
     else:
       print('not prime')
num=int(input('enter your number')) 
fun ()