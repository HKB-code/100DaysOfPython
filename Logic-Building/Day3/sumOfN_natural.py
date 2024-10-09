def sum_of_nNatural_numbers():
  try:
    number = int(input("Enter a number: "))
  except ValueError:
    print("Invalid number...")
  
  return number*(number+1)//2

value = sum_of_nNatural_numbers()
print(value)
