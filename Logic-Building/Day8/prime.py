def isPrime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True
    
x = isPrime(31)
print(x)


#Sieve of eratosthenes

def soe(limit):
  primes = [True] * (limit+1)
  p=2
  while(p*p<=limit):
    if primes[p]:
      for i in range(p*p,limit+1,p):
        primes[i] = False
    p+=1
  
  prime_numbers = [p for p in range(2,limit+1) if primes[p]]
  return prime_numbers

z = soe(50)
print(z)