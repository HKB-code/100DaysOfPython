# 1.
for i in range(1,6):
  line = ""
  for j in range(1,i+1):
    line+=str(j)
  print(line)
  
  
  # 2.
for i in range(1,6):
    # space
    line=""
    for j in range(6-i):
      line+=" "
    # print(line)
    # *
    
    for k in range(2*i-1):
      line+="*"
    print(line)
      
      
# 3
# In inverted loop (start,stop,step), so have to take stop to 0: so that loop run from 6 to 1
for i in range(6,0,-1):
    # space
    line=""
    for j in range(6-i):
      line+=" "
    # print(line)
    # *
    
    for k in range(2*i-1):
      line+="*"
    print(line)


# 4.
for i in range(1,6):
  lines=""
  for j in range(6-i):
    lines+=" "
  for k in range(2*i-1):
    lines+=str(j)
  print(lines)
  
  
# 5
for i in range(1,6):
  lines=""
  for j in range(6-i):
    lines+=" "
  for k in range(2*i-1):
    lines+=str(k+1)
  print(lines)
  
  
  
# 6
for i in range(5,0,-1):
  lines=""
  for j in range(6-i):
    lines+=" "
  for k in range(2*i-1):
    lines+=str(k+1)
  print(lines)
