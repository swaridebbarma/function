#meraki.q4
def fun ():
  numbers = [3, 5, 7, 34, 2, 89, 2, 5]
  i=0
  max=0
  while i<len(numbers):
      if numbers[i]> max:
          max=numbers[i]
      i+=1
  print(max)
fun ()
