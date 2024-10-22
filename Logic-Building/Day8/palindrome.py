import re
def isPalindrome(str1,str2):
  str1 = str1.lower()
  str1 = re.sub(r'[^a-zA-a0-9]',"",str1)
  
  str2 = str2.lower()
  str2 = re.sub(r'[^a-zA-a0-9]',"",str2)
  
  if len(str1)!=len(str2):
    return False
  else:
    estr = list(str1)
    print(estr)
    
    for word in estr:
      if word not in str2:
        return False
    
      else:
        return True      
      
x = isPalindrome("Na* N","Na* N")
print(x)
