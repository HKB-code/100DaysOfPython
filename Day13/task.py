import random
from maths import add

#  use debugger why it is not printing the whole list...
# def mutate(a_list):
#   b_list = []
#   new_item = 0
#   for item in a_list:
#     new_item = item*2
#     new_item +=random.randint(1,3)
#     new_item = add(new_item,item)
#   b_list.append(new_item)
#   print(b_list)
  
  
# mutate([1,2,3,5,8,13])

# /////////////
def mutate(a_list):
  b_list = []
  new_item = 0
  for item in a_list:
    new_item = item*2
    new_item +=random.randint(1,3)
    new_item = add(new_item,item)
    b_list.append(new_item)
  print(b_list)
  
  
mutate([1,2,3,5,8,13])