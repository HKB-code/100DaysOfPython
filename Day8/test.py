def greet():
  print("Hello")
  print("how do you do")
  print("Isn't the weather nice?")

greet()

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"how do you do {name}")
  
greet_with_name("Harshil")

# Now the argument is the actual piece of data that's going to be passed over to this function when it's

# being called, whereas the parameter is the name of that data,

# and we use the parameter inside the function to refer to it and to do things with it.

# Exercise-1
def num_Of_Weeks_Left(age):
  weeks = (90-age)*52
  print(f"You have {weeks} left.")

num_Of_Weeks_Left(65)

# Functions with more tahn 1 inputs

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Harshil","BWM")
greet_with(name="Harshil",location="BWM")