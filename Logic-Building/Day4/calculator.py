def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
options = {
  1:"*",
  2:"-",
  3:"+",
  4:"/"
}
def calculation(n1,n2,oper):
  if(oper=="*"):
    return mul(n1,n2)
  elif (oper=="+"):
    return add(n1,n2)
  elif oper=="-":
    return sub(n1,n2)
  elif oper=="/":
    if(n2==0):
      return "cannot divide by zero"
    elif(n1==0):
      return 0
    return div(n1,n2)


n1 = int(input("Enter the first number: "))

def calc():
  
  for symabol in options:
    print(options[symabol])
  sym = (input("pick the operation: \n"))
  n2 = int(input("Enter the second number: "))
  answer = calculation(n1,n2,sym)
  print(f"here is the answer: {answer}")
  return answer
  
answer = calc()
repeat = input("want to continue,Type 'yes' or 'no'...\n").lower()
if(repeat =='yes'):
  n1 = answer
  calc()
