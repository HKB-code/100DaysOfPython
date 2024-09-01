import random
# for i in range(5):
#   print(i)
#   friends = ["Rolf", "Jen", "Anne"]
# print(friends[0])
# n = int(input("enter number"))
# strNumber=""
# for i in range(n+1):
#   if(i>0):
#     strNumber += str(i)
# print(strNumber)
# fruits = ["Mango","apple","grapes"]
# for fruit in fruits:
#   print(fruit+"pie")
# for i in range(0,20,2):
#   print(i)
  
  
  # sum(iterable, start)
  # max(n1, n2, n3, ...)
# Or:
# max(iterable)

# st_score = [212,89,112,150,56,95,210]
# hig_score = st_score[0]
# for h in st_score:
#   if hig_score<h:
#     hig_score=h
# print(hig_score)

# z =0
# for i in range(1,101):
#   z+=i
# print(z)

# for i in range(1,101):
#     if i%5==0 and i%3==0:
#         print("FizzBuzz")
#     elif i%5==0:
#         print("Buzz")
#     elif  i%3==0:
#         print("Fizz")
#     else:
#         print(i)
friends = ["Harshil","peter","sam","jhon"]
print(friends[random.randint(0,len(friends))])
print(random.choice(friends))
print(random.choices(friends))