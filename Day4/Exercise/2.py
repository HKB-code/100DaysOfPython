# Question: Complete the script so that it produces the expected output. Please use my_range  as input data. my_range = range(1,21)

# using list comprehension: List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# syntax :      [expression for item in iterable if condition == True]
my_range = range(1,21)
list = [ x*10 for x in my_range ]
print(list)

# my_range = range(10,210,10)
# print(list(my_range))

# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
# new_lists = ["apple","banana","cherry"]
# new_lists = ["hello" for x in new_lists]
# print(new_lists)
