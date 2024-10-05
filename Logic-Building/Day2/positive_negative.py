def is_positive_or_negative():
  try:
     n = int(input("Enter the number you want to check if its is negative or positive...."))
  except ValueError:
    print("Invalid number.....")
    return
    
  if n==0:
    print("You entered zero")
    
  elif (n>=1):
    print("Its a positive number.")
  elif (n<0):
    print("Its a negative number.")
    
    