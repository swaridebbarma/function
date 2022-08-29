#Q1
def eligibleforvote(age):
    if age>=18:
        print("you are eligible")
    else:
        print("not eligible")
age=int(input("enter"))
eligibleforvote(age)