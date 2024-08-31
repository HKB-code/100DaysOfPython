# Create a script that generates and prints a list of numbers from 1 to 20. Please do not create the list manually.


# Ans: 
# The list() function is used to convert an iterable (such as a string , tuple or dictionary) into a list.It takes an iterable as an argument and returns a list with each element of the iterable as an itrm in the list.

# The python range() function returns a sequence of numbers, in given a range. The most common use of it is to iterate sequences on a sequence of numbers using python loops.


# Syntax: range(start, stop, step)

# Parameter :

# start: [ optional ] start value of the sequence
# stop: next value after the end value of the sequence
# step: [ optional ] integer value, denoting the difference between any two numbers in the sequence
# Return : Returns an object that represents a sequence of numbers


my_range = range(1,21)
print(list(my_range))
print(list(1))