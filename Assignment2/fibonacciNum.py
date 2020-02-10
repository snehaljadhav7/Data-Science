#!/bin/python3
def fibonacci(number):
   i = 1
   prev_prev = 1
   prev = 0
   for num in range(number):
       fibonacci_number = prev_prev + prev
       prev_prev = prev
       prev = fibonacci_number
     
   print(fibonacci_number)
fibonacci(25)

