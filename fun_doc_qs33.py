#doc.q33
def fun(bmi):
    if bmi > 30:
        return "obese"
    if bmi <= 18.5:
        return "underwight"
    if bmi <= 25.0:
        return "normal"
    if bmi <= 30.0:
        return "overwight"
    bmi= weight / height2
bmi=int(input("enter no:-"))
print(fun(bmi))