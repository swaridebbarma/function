
# sp=input('enter your password')
# def fun(sp):
#     i=0
#     while i<=len(sp):
#         if (sp>='a' and sp<='z' or sp<='A' and sp>='Z') or (sp<='0' or sp>='9') or (sp=='#',sp=='@',sp=='&'):
# 	        if len(sp)>=1 and len(sp)<=8:
# 		        print('strong password')
# 	        else:
# 		        print('wrong password')
#         else:
# 	        print('enter your password')
#         i+=1
# fun(sp)

# def sum(**a):
#     print(a)
# sum(a=7,b=5,c=7)

# def sum(*a):
#     print(a)
# sum(2,4,3)

# def sum_cheak(limit):
#     i=1
#     s=0
#     s1=0
#     while i<=(limit):
#         if i%2==0:
#             s=i+s
#         else:
#             s1=s1+i
#         i+=1
#     print("even:",s)
#     print("odd",s1)
# limit=int(input("enret:"))
# sum_cheak(limit)
            
# n=int(input("enter no"))  
# i=1
# while i<=n:
#     print(i)
#     i+=1       

# n=input("enter no")  
# a=input("enter")
# b=""

# def fun (x,y):
#     a=x+y
#     def fun2(x,y):
#         b=x*y
#         print(b)
#     fun(3,3)
#     print(a)
# fun(3,3)
def match_words(list):  
    ctr = 0    
    for w in list:  
        if len(w) > 1 and w[0] == w[-1]:  
          ctr += 1  
    return ctr 
list=['abc', 'xyz', 'aba', '1221']      
print(match_words(list))