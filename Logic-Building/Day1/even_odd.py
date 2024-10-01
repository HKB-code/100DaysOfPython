def is_even_or_odd():
  try:
     num = int(input("Write a number... "))
  except ValueError:
     print("Invalid number...")
     return
    
  if num%2==0:
    print("even")
  else:
    print("odd")
    
is_even_or_odd()