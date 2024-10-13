x = ['a','i','e','o','u']
n = "hello my name is uuu"
def checkV(str):
  count = 0
  z = str.split(" ")
  for i in z:
    c = list(i)
    for letter in c:
      if letter in x:
        count+=1
    
    # count+=1
    
  print(count)

checkV(n)


def checkV2(s):
    vowels = set('aeiou')
    count = 0
    for word in s.split():
        for letter in word:
            if letter.lower() in vowels:
                count += 1
    print(count)

n = "hello my name is uuu"
checkV2(n)



# /////////////////////////////////////////////
# A set in Python is an unordered collection of unique elements. Here are some key points to understand about sets:

# Uniqueness: A set cannot contain duplicate values. If you try to add the same element multiple times, it will only appear once in the set.
# Order: Unlike lists or tuples, sets do not maintain any specific order. The elements are stored in an arbitrary order.
# Creation: You can create a set using curly braces {} or by using the set() constructor. For example:
my_set1 = {1, 2, 3}  # Creating a set directly
another_set1 = set([3, 4, 5])  # Creating a set from a list

# Common Operations:
# Adding elements: Use the add() method to add a single element, or the update() method to add multiple elements.
# Removing elements: Use the remove() or discard() method.
# Checking membership: You can use the in keyword to check if an element exists in the set.
# Set operations: Sets support union, intersection, and difference operations.

# Use Cases:
# Removing duplicates from a list: Convert the list to a set and then back to a list.
# Checking for unique elements: Sets are great for ensuring uniqueness.
# Mathematical operations: Sets are useful for solving problems involving unions, intersections, and differences.

# Creating a set
my_set = {1, 2, 3, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding an element
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Checking membership
print(3 in my_set)  # Output: True

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
print(intersection_set)  # Output: {3}
print(difference_set)  # Output: {1, 2}
