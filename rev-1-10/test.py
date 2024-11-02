def upperWORD(str):
  estr = str.split()
  upstr=""
  # Method-1
  
  # for i in range(len(estr)):
  #   upstr += estr[i][0].upper() + estr[i][1:] + " "
    
  # print(upstr)
  for word in estr:
    upstr +=word[0].upper()+ word[1:]+" "
  print(upstr)
    
upperWORD("harshil jain")
n = int(input("Enter number of entries..."))
z = {input(f"Enter the key {i+1}"): input(f"Enter the value {i+1}") for i in range(n)}
print(z)
dict1={'a':1,'b':2}
dict2={'b':3,'d':4}
for key, value in dict2.items():
  if key in dict1:
    if isinstance(dict1[key],list):
      dict1[key].append(value)
    else:
       dict1[key] = [dict1[key],value]
  else:
   dict1[key] = value
print(dict1)