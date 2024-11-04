# import random
# def guess_number():
#   lists = list(range(1,101))
#   # print(lists)
#   key_number = random.choice(lists)
#   return key_number 

# def choose_level():
#   level = input("Choose a difficulty. Type 'easy' or 'hard':")
#   lives = 10 if level=='easy' else 5
#   return lives

# attempts = choose_level()
# print(attempts)
# number = guess_number()
# print(number)


# guess_true=True
# while guess_true and attempts>0:
  
#   guess = int(input("Make a guess: "))
#   if number!=guess:
#      attempts-=1
#      if attempts>=1:
#       if number>guess:
#        print("Too Low")
#        print("Guess Again")
#        print(f"You have {attempts} remaining to guess the number")
#       elif number<guess:
#         print("Too High")
#         print("Guess Again")
#         print(f"You have {attempts} remaining to guess the number")
#      elif attempts<1:
#        print("You've lost the game....")
        
#   elif number==guess:
#     print(f"You got it! The answer was {number}.")
#     guess_true=False
        
        
# Refactor        
from random import randint
  
EASY_LEVEL_TURNS = 10    
HARD_LEVEL_TURNS = 5
       
def check_answer(user_guess,acutal_answer,turns):
  """Checks answer against guess, returns the number of turns remaining."""
  if user_guess>acutal_answer:
    print("Too High")
    return turns - 1
  elif user_guess<acutal_answer:
    print("Too Low")
    return turns - 1 
  else:
    print(f"You got it! The answer was {acutal_answer}.")
    
    
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
  
  if level=="easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
    
    
def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = randint(1,100)
  turns =set_difficulty()
  print(f"You have {turns} attempts remaining to guess the number..")

  guess =0
  while guess!=answer:
    guess = int(input("Make a guess: "))

    turns = check_answer(guess,answer,turns)
    print(f"You have {turns} remaining to guess the number")
    if turns==0:
       print("You've lost the game....")
       return
    elif guess!=answer:
      print("Guess Again")
      
      
      
    


