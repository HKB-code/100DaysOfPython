# from logo import logo,vs
# from random import choice
# from game_data import data

# def datas():
#   return  choice(data)



# def data_format(dataInputs):
#   return f"{dataInputs['name']}, a {dataInputs['description']}, from {dataInputs["country"]}"

# def compare(user_inputs,compare_A,compare_B):
#   if user_inputs=="a" and compare_A["follower_count"]> compare_B['follower_count']:
#     return 1
#   elif user_inputs=="b" and compare_A["follower_count"]< compare_B["follower_count"]:
#     return 1
  
#   return 0


# def play():
#   print(logo)
#   should_continue = True
#   final_score = 0
#   a = datas()
#   b = datas() 
#   if a==b:
#         b =datas() 
  
#   while should_continue:
#     print("Compare A:",data_format(a))
#     print(vs)
#     print("Compare B:", data_format(b))
#     user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
#     current_score = compare(user_inputs=user_input,compare_A=a,compare_B=b)
#     if current_score==0:
#       should_continue = False
#       print(f"Your final score: {final_score}")
#     else:
#       final_score+=1
#       print(f"You got it current score {final_score}")
#       a=b
      
#       b= datas()
#       if a==b:
#         b =datas()
      
      
    

    
    
# play()
  
  
  
  
  

# ////////////////////////////

# Display art
from logo import logo,vs
from random import choice
from game_data import data


#Format the account data into printable format
def formate_data(account):
  """Format the account data into printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess,a_followers,b_followers):
  """Take a user's guess and the follower counts and returns if they got it right"""
  if a_followers>b_followers:
   
      return user_guess=="a"
  else:
      return user_guess=="b"
    
print(logo)
  # Generate a random account from the game data
account_a  = choice(data)
account_b = choice(data)
if account_a==account_b:
  account_b = choice(data)
# score keeping.
score=0
game_should_continue = True
# make the game repeatable

while  game_should_continue:


  print(f"Compare A: {formate_data(account_a)}")
  print(vs)
  print(f"Compare B: {formate_data(account_b)}")






  # Ask user for guess
  guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

#  clear screen
  print("\n"*20)
  print(logo)
  
  

  # check if user is correct
  # -Get followers count of each amount
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]




  #  Give user feedback on their guess.
  is_correct = check_answer(guess,a_follower_count,b_follower_count)
  if is_correct:
    score+=1
    print(f"You're right!, Current Score {score}")
# making  account at position B become the next account at position A.
    
    account_a = account_b
    account_b = choice(data)
  else:
    print(f"Sorry, that's wrong, Final score {score}")
    game_should_continue=False
  
  
  





