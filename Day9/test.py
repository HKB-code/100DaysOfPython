programming_dictionary={
  'Bug':"An error ina aprogram that prevents the program from running as expected ",
  'Functions':"A piece of code that you can easily call over and over again",
   'Loop':"The action of doing something over and over again" ,
   123: "integer"
   
}
# when you're trying to retrieve the data from that key,you also have to make sure that you provide the key in its actual data type.
print(programming_dictionary["Bug"])
print(programming_dictionary[123])

programming_dictionary["Bool"] = "True/False"

print(programming_dictionary)


empty_dictionary = {}


# wipe the existing dictionary
# programming_dictionary = {}
# That can be really useful if you wanted to clear out a user's progress,

# or for example, if a game restarts, then all the scores and stats will probably have to be wiped empty.

# So this is one way that you could do that.
# print(programming_dictionary)


# edit an item in an dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])




capitals = {
  "France": "Paris",
  "Germany":"Berlin"
  }

# Nested list in dictionary
# travel_vlog = {
#   "France": ["Paris","Lille","Dijon"],
#   "Germany": ["Stuttgart","Berlin"]
# }

# Print lille
# print(travel_vlog["France"][1])

# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

travel_vlog = {
  "France": {
    "num_times_visited":8,
    "cities_visited":["Paris","Lille","Dijon"]
    },
  "Germany": {
    "num_times_visited":12,
    "cities_visited": ["Hamburg","Stuttgart","Berlin"]
  }
  }
print(travel_vlog["Germany"]["cities_visited"][1])

num_entries = int(input("Enter the number of entries you want to add: "))

use_dict = {input(f"Enter the key {i+1}: "): input(f"Enter the value {i+1}: ") for i in range(num_entries)}
print(use_dict)
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# print({**dict1,**dict2,**use_dict})
for key,value in dict2.items():
  print(key,value)
  dict1[key]= value
print(dict1) 

dict3= {'a': 1, 'b': 2}
dict4 = {'b': 3, 'd': 4,"b":6}

for key,value in dict4.items():
  if key in dict3:
    if isinstance(dict3[key],list):
      dict3[key].append(value)
    else:
      dict3[key] = [dict3[key],value]
  else:
    dict3[key] =value
print(dict3)