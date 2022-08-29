# def fun():
#     string_name = "Shakrudin"
#     print (len(string_name))
# fun()

# def check_count():
#     string_name = "Rishabh Verma"
#     print (len(string_name))
# check_count()

# def fun():
#     string_name = "swari"
#     if "s" in string_name:
#         print ("s hai")
#     else:
#         print ("s nahi hai")
# fun()

# def check():
#     string_name="navgurukul"
#     print ("n" in string_name)
#     print (type("n" in string_name))
# check()

# sp=input('enter your password')
# sp='rahul$%verma12!' 
# def fun(sp):
#     i=0
#     while i<=len(sp):
#         if (sp>='a' and sp<='z' or sp<='A' and sp>='Z') or (sp<='0' or sp>='9') or (sp=='$',sp=='@',sp=='&'):
# 	        if len(sp)>=1 and len(sp)<=16:
# 		        print('strong password')
# 	        else:
# 		        print(' wrong password')
#         else:
# 	        print('weak password')
#         i+=1
# fun(sp)


sp=input("enter sp:")
def func(sp):
    if (sp>='a' and sp<='z' or sp<='A' and sp>='Z') or (sp<='0' or sp>='9') or (sp=='$',sp=='@',sp=='&'):
        if len(sp)>=6 and len(sp)<=16:
            print('strong password')
        else:
            print(' wrong password')
    else:
        print('weak password')
func(sp)



#more_qs3