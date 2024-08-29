print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10,12, 0r 15?\n"))
if tip!=10 or tip!=12 or tip!=15:
  print("You chose wrong tip value")
else: 
  split =int(input("How many people to split the bill?\n"))
  amount = (bill*(tip/100))
  total_amount = round((bill*(tip/100))/split,2)
  print(f"The total amount is {amount},Each person should pay: {total_amount}")