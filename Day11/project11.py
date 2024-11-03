import random
from art import logo

# Method-1
# play = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# def blackJack():
#   cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
#   # weights=[11,1,1,1,1,1,1,1,1,10,10,10,10]
#   # user_list = []
#   # computer_list = []
#   current_score = {}
#   # For checking certain conditions like : [11,11]
#   # user_list = random.choices(cards,weights=weights,k=2) 
#   user_list = random.choices(cards,k=2)  
   
#   computer_list = random.choices(cards,k=2)  
  
#   print(logo)
#   if  user_list==[11,10] or user_list==[10,11]:
#       current_score['user'] = 0
#       print(f"Your final hand: {user_list}, final score: {current_score['user']}")
#       print(f"Computer's first card: {computer_list[0]}")
#       print("You hit the BlackJack!")
#       play_again = input ("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
#       if play_again=='y':
#        blackJack()   
      
#   elif computer_list==[11,10] or computer_list==[10,11]:
#       current_score['computer'] = 0
#       print(f"Your cards: {user_list}, current score: {current_score['user']}")
#       print(f"Computer's final card: {computer_list}")
#       print("Computer hit the BlackJack!")
#       play_again = input ("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
#       if play_again=='y':
#          blackJack()   
      

#   elif user_list!=[11,10] and computer_list!=[11,10]:
#     current_score['user'] = sum(user_list)
#     current_score['computer'] = sum(computer_list)
#     if current_score['user']>21:
#       print(f"Your final hand: {user_list}, final score: {current_score['user']}")
#       print(f"Computer's final hand: {computer_list}, final score: {current_score['computer']}")
#       print('You Lose')
#     else:
     
#      if current_score['user']>=20:
#       cards[0] = 1
#      if current_score['computer']>=20:
#       cards[0] =1
#      print(f"Your cards: {user_list}, current score: {current_score['user']}")
#      print(f"Computer's first card: {computer_list[0]}")
#      want_another_card = True;
#   # correct a BUG here, The Bug is stopping the while loop in the code, the BUG:while want_another_card and current_score['user']<21:
     
#      while want_another_card and current_score['user']<=21:
#       another_Card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#       if another_Card =='n':
#         while current_score['computer']<17:
#          computer_list.append(random.choice(cards))
#          current_score['computer'] = sum(computer_list)
#         print(f"Your final hand: {user_list}, final score: {current_score['user']}")
#         print(f"Computer's final hand: {computer_list}, final score: {current_score['computer']}")
        
        
#         want_another_card=False
        
        
        
#       elif another_Card=='y':
#         user_list.append(random.choice(cards))
#         current_score['user'] = sum(user_list)
#         if current_score['user']>21:  
#           print(f"Your final hand: {user_list}, final score: {current_score['user']}")
#           print(f"Computer's final hand: {computer_list}, final score: {current_score['computer']}")
#           print("You went over, you lose")
#           want_another_card=False
          
#         else:
#             print(f"Your cards: {user_list}, current score: {current_score['user']}")
#             print(f"Computer's first card: {computer_list[0]}")
            
 
#   if current_score['user']<=21 and current_score['computer']<=21:
#      if current_score['user']>current_score['computer']:
#       print("You win")
#      elif current_score['user']<current_score['computer']:
#         print('You lose')
#      elif current_score['user']==current_score['computer']:
#          print("Draw")
#   elif current_score['computer']>21:
#      print('computer went over, You win')
#   play_again = input ("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
#   if play_again=='y':
#      blackJack()           
            
# if play =='y':
#   blackJack()
 
 
#  Method-2

def deal_card():
  """Returns a random card from deck"""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card
  
def calculate_card(cards):
  """Take a list of cards and return the score calculated from the cards"""
  # if 11 in cards and 10 in cards and len(cards )==2:
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(u_score,c_score):
  if u_score==c_score:
    return "Draw"
  elif u_score==0:
    return "Win with the BlackJack"
  elif c_score == 0:
    return "Lose, opponent has BlackJack"
  elif u_score>21:
    return "You went over. You lose"
  elif c_score>21:
    return "Opponent went over. You win"
  elif u_score>c_score:
    return "You win"
  else:
    return "You lose"
  
def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  computer_score =-1
  user_score = -1


# += ,extend(...)
  for _ in range(2):
   user_cards.append(deal_card())
   computer_cards.append(deal_card())
  
  while not is_game_over:
   user_score = calculate_card(user_cards)
   computer_score = calculate_card(computer_cards)
   print(f"Your cards: {user_cards}, current score: {user_score}")
   print(f"Computer's first cards: {computer_cards[0]}")

   if user_score==0 or computer_score==0 or user_score>21:
    is_game_over = True
   else:
    user_should_deal = input("Type 'Y' to get another card, type 'N' to pass:\n").lower()
    if user_should_deal=='y':
     user_cards.append(deal_card())
    else:
      is_game_over = True
    
   while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_card(computer_score)

  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(u_score=user_score,c_score=computer_score))


while input("Do you want to play another game. Type 'Y' for yes or 'N' for no ").lower =='y':
  play_game()