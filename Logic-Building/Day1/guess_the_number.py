# version:1
import random
# def random_number():
#   number = random.randint(1,10)
#   # print(number)
#   return number

# attempts =5
# number = random_number()
# def play_game():
#   global number,attempts,should_continue
#   guess = int(input("Guess the number: "))
#   if number!=guess:
#     attempts-=1
#     if guess<number:
#       print("Too low")
#     elif guess>number:
#       print("Too High")
#     if attempts>=1: 
#      print(f"You.ve {attempts} attempts left..")
#     else:
#       print("You lost the game")
#   elif guess==number:
#     print("You have got the answer...")
#     should_continue=False
  
# print("Welcome to the Guess the number...")
# print(f"You have {attempts} attempts.... ")
# should_continue=True
# while attempts>0 and should_continue:
#   play_game()
  
# Problems in version 1: 
# a.input validation
# b. global variables
def random_number():
  return random.randint(1,10)
def play_game(number,attempts):
  while attempts>0:
    try:
      guess = int(input("Guess the number.. "))
      if 1>guess or guess>10:
        print("Please enter a number between 1 and 10 ")
        continue
    except ValueError:
      input("Invalid input.Please enter a number.")
    if guess!=number:
      attempts-=1
      if guess<number:
       print("Too low")
      elif guess>number:
       print("Too High")
      if attempts>=1: 
       print(f"You.ve {attempts} attempts left..")
      else:
       print("You lost the game")
    elif guess==number:
     print("You have got the answer...")
     return
  
def main():
  print("Welcome to the Guess the number...")
  attempts = 5
  number = random_number()
  print(f"You have {attempts} attempts.")
  play_game(number, attempts)
  
  
if __name__ == "__main__":
    main()
