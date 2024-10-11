def largest_three(n1,n2,n3):
  if n1==n2==n3:
    print("oops all the number are same..")
    return 0
  else: 
      if (n1>n2) and (n1>n3):
        return n1
      elif (n2>n1) and (n2>n3):
       return n2
      else:
        return n3  


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

largest = largest_three(n1,n2,n3)
print(f"The largest number is : {largest}")