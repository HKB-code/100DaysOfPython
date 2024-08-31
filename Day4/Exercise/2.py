# Question: Complete the script so that it produces the expected output. Please use my_range  as input data. my_range = range(1,21)

# using list comprehension: List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
my_range = range(1,21)
list = [10* x for x in my_range ]
print(list)

# my_range = range(10,210,10)
# print(list(my_range))