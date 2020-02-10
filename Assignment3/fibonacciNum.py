#!/bin/python3
def fibonacci(number):
   i = 1
   prev_prev = 1
   prev = 0
   while i <= number:
       fibonacci_number = prev_prev + prev
       prev_prev = prev
       prev = fibonacci_number
       i = i + 1
   print(fibonacci_number)
fibonacci(25)
