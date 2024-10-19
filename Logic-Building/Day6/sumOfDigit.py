def sum():
  try: 
    n = int(input("Enter a Number: \n"))
    if n==0:
      return 0
  except ValueError:
    print("Please enter a valid numbert")
  sums=0
  while n>0:
    lastDigit = n%10
    sums+=lastDigit
    n = n//10
  return sums

x = sum()
print(x)