n = "hi my name is ....."

def revStr(str):
  x = list(str)
  rev = ('').join(x[::-1])
  return rev

value = revStr(n)
print(value)
rv=""
for i in range(len(n) - 1, -1, -1):
  rv+=n[i]
  print(i)
print(rv)

   