'''#!/bin/python3
def fibonacci3(n):
      if n > 1:
         return(fibonacci3(n-1) + fibonacci3(n-2))
      else:
         return n

for ele in range(10):
    print(fibonacci3(ele))'''


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 10
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
