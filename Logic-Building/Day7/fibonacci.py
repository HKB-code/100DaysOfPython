def fib(n):
  try:
   if int(n)!= n or n<0:
     raise ValueError
  except:
    print("Invalid Number...")
    return None
    
  if(n==0 or n==1):
   return 1
  else:
   return fib(n-1) + fib(n-2)
  
  
x = fib("a")
print(x)
