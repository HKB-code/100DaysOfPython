# What is try and except?
# The try and except blocks in Python are used for handling exceptions, which are errors that occur during the execution of a program. Here’s a brief overview:

#  # How try and except Work
# try Block: This block contains the code that might throw an exception. If an exception occurs, the rest of the code inside the try block is skipped.
# except Block: This block contains the code that runs if an exception occurs in the try block. It allows you to handle the error gracefully without crashing the program.

try:
    # Code that might throw an exception
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"The result is {result}")
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("Error: You cannot divide by zero.")
except ValueError:
    # Code that runs if a ValueError occurs
    print("Error: Invalid input. Please enter a valid number.")

# Explanation
# try Block: The code inside the try block attempts to convert user input to an integer and then divides 10 by that number.
# except ZeroDivisionError: If the user enters 0, a ZeroDivisionError occurs, and this block runs, printing an error message.
# except ValueError: If the user enters something that isn’t a number (like a string), a ValueError occurs, and this block runs, printing an error message.




# Additional Clauses
# else Block: Runs if no exceptions are raised in the try block.
# finally Block: Runs no matter what, whether an exception occurred or not. It’s often used for cleanup actions like closing files.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"The result is {result}")
finally:
    print("This block runs no matter what.")



# //////////////////////////////
# if __name__ == "__main__":
    # main()
    
    # The line if __name__ == "__main__": main() is a common Python idiom used to ensure that certain code is only executed when the script is run directly, and not when it is imported as a module in another script.
#     Explanation
# __name__: This is a special built-in variable in Python. When a Python script is run directly, __name__ is set to "__main__". However, when the script is imported as a module in another script, __name__ is set to the name of the script/module.
# if __name__ == "__main__":: This condition checks whether the script is being run directly or being imported. If it is being run directly, the code inside this block will execute.
# main(): This is typically the main function of the script that contains the primary logic of the program.
    
    
def main():
   print("Hello, World!")

if __name__ == "__main__":
    main()

# How It Works
# When you run the script directly (e.g., python script.py), __name__ is set to "__main__", so main() is called, and “Hello, World!” is printed.
# If you import this script in another script (e.g., import script), __name__ is set to "script", and main() is not called automatically.
# Why Use It?
# This idiom is useful for:

# Organizing Code: It helps in organizing code by separating the main execution logic from function definitions.
# Reusability: It allows the script to be reused as a module without executing the main code unintentionally.
# Testing: It makes it easier to test functions in the script without running the main code.


#/////////////////////////////
# Example: Using return to Exit a Loop
# Here’s a simple function that searches for a specific number in a list. If the number is found, the function returns the index of the number and exits the loop. If the number is not found, it returns -1.
def find_number(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index  # Exit the loop and return the index
    return -1  # Return -1 if the number is not found

# Example usage
numbers = [10, 20, 30, 40, 50]
target = 30
result = find_number(numbers, target)
if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found")


# The enumerate function in Python is a built-in function that adds a counter to an iterable and returns it as an enumerate object. This can be very useful when you need both the index and the value of items in a list or other iterable.
# enumerate(iterable, start=0)

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


word = "hello"
for index, letter in enumerate(word):
    print(index, letter)
