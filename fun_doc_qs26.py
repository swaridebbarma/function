#doc.q26
def fizz_buzz():
    if num%3==0 and num%5==0:
        print("fizzbuzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
        return num
num=int(input("enter number"))
fizz_buzz()



"""def fizzler(num):

    if num % 3 != 0 and num % 5 != 0:

       return num

    if num % 3 == 0 and num % 5 == 0:

       return "FizzBuzz"

    if num % 3 == 0:

       return "Fizz"

       return "Buzz"
if __name__ == "__main__":
    num= int(input("Enter a num: "))

print(fizzler(num))"""

