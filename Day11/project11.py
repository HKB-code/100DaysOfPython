import random
from art import logo

# Method-1
play = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
def blackJack():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  # weights=[11,1,1,1,1,1,1,1,1,10,10,10,10]
  user_list = []
  computer_list = []
  current_score = {}
  # For checking certain conditions like : [11,11]
  # user_list = random.choices(cards,weights=weights,k=2) 
  user_list = random.choices(cards,k=2)  
   
  computer_list = random.choices(cards,k=2)  
  
  print(logo)
  if  user_list==[11,10] or user_list==[10,11]:
      current_score['user'] = 0
      print(f"Your final hand: {user_list}, final score: {current_score['user']}")
      print(f"Computer's first card: {computer_list[0]}")
      print("You hit the BlackJack!")
      play_again = input ("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
      if play_again=='y':
       blackJack()   
      
  elif computer_list==[11,10] or computer_list==[10,11]:
      current_score['computer'] = 0
      print(f"Your cards: {user_list}, current score: {current_score['user']}")
      print(f"Computer's final card: {computer_list}")
      print("Computer hit the BlackJack!")
      play_again = input ("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
      if play_again=='y':
         blackJack()   
      

  elif user_list!=[11,10] and computer_list!=[11,10]:
    current_score['user'] = sum(user_list)
    current_score['computer'] = sum(computer_list)
    if current_score['user']>21:
      print(f"Your final hand: {user_list}, final score: {current_score['user']}")
      print(f"Computer's final hand: {computer_list}, final score: {current_score['computer']}")
      print('You Lose')
    else:
     
     if current_score['user']>=20:
      cards[0] = 1
     if current_score['computer']>=20:
      cards[0] =1
     print(f"Your cards: {user_list}, current score: {current_score['user']}")
     print(f"Computer's first card: {computer_list[0]}")
     want_another_card = True;
     while want_another_card and current_score['user']<21:
      another_Card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_Card =='n':
        while current_score['computer']<17:
         computer_list.append(random.choice(cards))
         current_score['computer'] = sum(computer_list)
        print(f"Your final hand: {user_list}, final score: {current_score['user']}")
        print(f"Computer's final hand: {computer_list}, final score: {current_score['computer']}")
        
        
        want_another_card=False
        
        
        
      elif another_Card=='y':
        user_list.append(random.choice(cards))
        current_score['user'] = sum(user_list)
        if current_score['user']>21:  
          print(f"Your final hand: {user_list}, final score: {current_score['user']}")
          print(f"Computer's final hand: {computer_list}, final score: {current_score['computer']}")
          print("You went over, you lose")
          want_another_card=False
          
        else:
            print(f"Your cards: {user_list}, current score: {current_score['user']}")
            print(f"Computer's first card: {computer_list[0]}")
  if current_score['user']<=21 and current_score['computer']<=21:
     if current_score['user']>current_score['computer']:
      print("You win")
     elif current_score['user']<current_score['computer']:
        print('You lose')
     elif current_score['user']==current_score['computer']:
         print("Draw")
  elif current_score['computer']>21:
     print('computer went over, You win')
  play_again = input ("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
  if play_again=='y':
     blackJack()           
            
if play =='y':
  blackJack()
 
 
#  Method-2
