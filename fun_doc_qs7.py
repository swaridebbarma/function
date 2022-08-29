def calculate_bmi(bmi):
    if bmi <= 18.5:
        return "Underwight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overwight"
    if bmi > 30:
        return "Obese"
bmi=int(input("enter no:-"))
print(calculate_bmi(bmi))