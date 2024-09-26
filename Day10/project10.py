# logo=r'''
#  _____________________
# |  _________________  |
# | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
# |_____________________|  
# '''
# print(logo)
# should_continue= True
# n1 = float(input("What is the first number?: "))
# option = input("*\n+\n-\n/\nPick an operation? ")
# n2 = float(input("What is the next number?:"))
# value = {}
# def add(n1,n2):
#   return n1+n2
# def sub(n1,n2):
#   return n1-n2
# def mul(n1,n2):
#   return n1*n2
# def div(n1,n2):
#   return n1/n2

# def calculate(n1,n2,option):
#   if option=="*":
#    return mul(n1,n2)
#   elif option=="+":
#    return add(n1,n2)
#   elif option=="-":
#    return sub(n1,n2)
#   elif option=="/":
#     if n2==0:
#       return "Error! Division by zero."
#     return div(n1,n2)
  

# value['sum_total']=calculate(n1,n2,option=option)


# while should_continue:

#   repeat= input(f"Type 'y' to continue calculating with {value['sum_total']}, or type 'n' to start a new calculation:").lower()
#   if repeat == 'y':
#    n2 = float(input("What is the next number?:"))
#    option = input("*\n+\n-\n/\nPick an operation? ")
#    value["sum_total"] =calculate(n1=value["sum_total"],n2=n2,option=option)
   
     
#   else:
#     should_continue=False
#     print(f"{value['sum_total']}")
 
# print(value)
# print(value["sum_total"])


# %% Using Recursion...

logo=r'''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|  
'''
print(logo)

def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
def calculate():
  print(logo)
  should_continue= True
  n1 = float(input("What is the first number?: "))
  option = {
  "*": mul,
  "+":add,
  "/":div,
  "-":sub
   }
  while should_continue:
    for symbol in option:
     print(symbol)
    symbol_pick = input("Pick an operation? ")
    n2 = float(input("What is the next number?:"))
    answer = option[symbol_pick](n1=n1,n2=n2)
    repeat= input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()
    if repeat =='y':
     n1 = answer
    else:
      should_continue=False
      calculate()
  
calculate()