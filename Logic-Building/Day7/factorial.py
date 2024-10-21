def factorial(n):
  try: 
    if int(n)!=n:
      raise ValueError
  except ValueError:
    print("Invalid Number...")
    return None
  if n==0:
    return 1
  else:
    return n  * factorial(n-1)
    
x = factorial(3)
print(x)

