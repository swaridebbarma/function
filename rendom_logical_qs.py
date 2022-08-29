# a=[1,2,3,4,5,]
# b=[]
# for i in a :
#     if i not in (4,5):
#         b.append(i)
# print(b)
# a=[1,2,3,4,5,6]
# i=0
# while i<len(a):
#     j=0
#     b=[]
#     while j<len(a):
#         s=a[i]+a[j]
#         b.append(s)
#         j+=1
#     i+=1
# print(b)

# num=[9,23,45,6,7,9]
# m=int(len(num)/2)
# i=0
# result=[]
# reverse_list=num[::-1]
# while (i!=len(num)):
#     result.append(reverse_list[i]+num[i])
#     i+=1
#     end_result=result[:m]
# print(end_result)

# a=[1,2,3,[4,5],6,[7,8]]
# i=0
# while i<len(a):
#     if type(a[i])!=list:
#         print(a[i])
#     else:
#         b=0
#         while b<len(a[i]):
#             if type (a[i])==list:
#                 print(a[i][b])
#             b+=1
#     i+=1


# a=3
# b=5
# c=a+b
# d=a-b
# e=a*b
# print(c,d,e)

# a = int(input("enter no"))
# b = int(input("enter no"))
# c=a//b
# d=a/b
# print(c)
# print(d)

# n=int(input("enter"))
# i=0
# while i<=n:
#     a=i*i
#     print(a)
#     i+=1
# a=[1,2,3,[4,5]]
# i=0
# while i<len(a):
#     if type(a[i])!=list:
#         print(a[i])
#     else:
#         j=0
#         while j<len(a[i]):
#             if type(a[i])==list:
#                 print(a[i][j])
#             j=j+1
#     i+=1


# a=int(input("enter"))
# i=1
# while i<=a:
#     print(i)
#     i+=1
# a=[1,2,3,[4,5,[6]]]
# i=0
# sum=0
# while i <len(a):
#     if type(a[i])==type([]):
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==type([]):
#                 k=0
#                 while k<len(a[i][j]):
#                     sum=sum+(a[i][j][k])
#                     k+=1
#             else:
#                 sum=sum+(a[i][j])  
#             j+=1
#     else:
#         sum=sum+(a[i])          
#     i+=1
# print(sum)        
                    
                    
# i=1
# while i<=200:
#   j=1
#   c=0
#  while j<=i:
#       if i%j==0:
#         c+=1
#       j+=1
#   if c==2:
#       print(i,'prime')
#   i+=1
  
# year=int(input('enter no'))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("lea year")
# else:
#     print("not leap year")
    
# a=int(input("enter no"))
# b=int(input("enter no"))
# c=int(input("enter no"))
# if a>b:
#     if a<c:
#         mediam=a
#     elif b>c:
#         mediam=b
#     else:
#         mediam=c
# else:
#     if a>c:
#         mediam=a
#     elif b<c:
#         mediam=b
#     else:
#         mediam=c
# print("The mediam is",mediam)

def ATM ():
    print("Welcome to UCO")
    print("enter your card here")
    language=input(".English\n.Hindi\nSelect your language")
    if language=='hindi' or language=='english':
            print('Thankyou for chosing this language ')
            pin=int(input("enter you four digit"))
            if pin==1234:
                pass
            transaction=input("withdraw\ndeposit\nbalance enquiry\nenter your transaction")
            amt=int(input("enter the amount"))
            if transaction=="withdraw":
                if amt<=10000:
                    print("your transaction is being processed wait a moment")
                    exit=input("remove your card")
                    if exit=="exit":
                        print("Thank you for visiting")
            else:
                print("you do not have sufficiant balance")
    elif transaction=="deposit":
            if amt>0:
                print("your transaction is being processed, please wait")
                if exit=="exit":
                    print("Thank you for visiting")
                else:
                    print("no cash")
            elif transaction=="balance enquiry":
                amt>0
    choose=input('enter saving')
    if choose=='saving':
            print("your transaction is being processed Please wait")
            exit=input("remove your card")
            if exit=="exit":
                print("Thankyou for visiting")
            else:
                print("incorrect pin code")
    else:
        print("please enter the respective language")
ATM()