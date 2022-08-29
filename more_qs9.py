"""def fun():
    n=int(input('enter number'))
    i=n
    s=0
    while i > 0:
	    s=s+(i%10)
	    i=i//10
    if n%s==0:
        print("True",s)
    else:
	    print('False')
# fun()"""

def check_harshad_no():
    a=1
    while a<=limit:
        i=a
        s=0 
        while i>0:
	        s=s+(i%10)
	        i=i//10
        if a%s==0:
            print(a,"True",s)
        a+=1
limit=int(input("enter limit no:"))
check_harshad_no()
#more_qs9