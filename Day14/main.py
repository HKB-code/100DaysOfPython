from logo import logo,vs
from random import choice
from game_data import data

def datas():
  return  choice(data)



def data_format(dataInputs):
  return f"{dataInputs['name']}, a {dataInputs['description']}, from {dataInputs["country"]}"

def compare(user_inputs,compare_A,compare_B):
  if user_inputs=="a" and compare_A["follower_count"]> compare_B['follower_count']:
    return 1
  elif user_inputs=="b" and compare_A["follower_count"]< compare_B["follower_count"]:
    return 1
  
  return 0


def play():
  print(logo)
  should_continue = True
  final_score = 0
  a = datas()
  b = datas() 
  if a==b:
        b =datas() 
  
  while should_continue:
    print("Compare A:",data_format(a))
    print(vs)
    print("Compare B:", data_format(b))
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    current_score = compare(user_inputs=user_input,compare_A=a,compare_B=b)
    if current_score==0:
      should_continue = False
      print(f"Your final score: {final_score}")
    else:
      final_score+=1
      print(f"You got it current score {final_score}")
      a=b
      
      b= datas()
      if a==b:
        b =datas()
      
      
    

    
    
play()
  
  
  
  
  



