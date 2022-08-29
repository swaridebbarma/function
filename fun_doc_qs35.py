#doc.q35
def fun(old):
    if old < 14:
        return("drink toddy")
    elif old < 18:
        return("drink coke")
    elif old >= 18 and old < 21:
        return ("drink beer")
    elif old >= 21:
        return ("drink whisky")
old=int(input("enter age:-"))
print(fun(old))