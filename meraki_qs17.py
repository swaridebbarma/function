#meraki.q17
def calcu (a,b, operation):
    if operation =="aad":
        c=a+b
        return c
    elif operation =="substract":
        c=a-b
        return c
    elif operation=="multply":
        c=a*b
        return c
    elif operation=="divide":
        c=a%b
        return c
a=int(input("enter"))
b=int(input("enter"))
aad_result=calcu(a,b,"aad")
print(aad_result)
sub_result=calcu(a,b,"substract")
print(sub_result)
mul_result=calcu(a,b,"multply")
print(mul_result)
div_result=calcu(a,b,"divide")
print(div_result)