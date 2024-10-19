import math
def isArmstrong():
  try:
    n = int(input("Enter a number: \n"))
  except ValueError:
    print("Please Enter a valid number...")
  sums = 0
  original_value = n
  while n>0:
    lastDigit = int(n%10)
    sums+= int(math.pow(lastDigit,3))
    print(sums)
    n = n//10
  print(sums)
  
  return original_value==sums

x = isArmstrong()
print(x)
