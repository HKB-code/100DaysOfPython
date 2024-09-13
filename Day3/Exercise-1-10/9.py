#Complete the script so that it prints out a list containing the last three elements of list letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# print(letters[-1:-3]) empty list
print(letters[-3:])

# Explanation: 
# [-3:]  means from the item with index -3  (i.e. h ) to the very last item of the list. When you don't put any index to the colon's right, everything is included, and upper-bound exclusivity is ignored.

# Understanding List Slicing
# * In Python, list slicing allows you to access a subset of elements from a list. The syntax is list[start:end], where:

# start is the index where the slice begins (inclusive).
# end is the index where the slice ends (exclusive).
# Negative Indices
# Negative indices count from the end of the list:

# -1 is the last element.
# -2 is the second last element, and so on.

# Here, letters[-1:-3] means:

# Start at index -1 (which is "j").
# End at index -3 (which is "h", but exclusive).
# Since the end index is before the start index, this slice returns an empty list.
# Breakdown of letters[-3:]
# -3 refers to the third last element ("h").
# The absence of an end index means it goes to the end of the list.
# So, letters[-3:] returns ["h", "i", "j"].