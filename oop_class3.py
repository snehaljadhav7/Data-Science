#!/bin/python3
class Car:
   wheels = 4 


   def __init__(self):
      self.mil = 10
      self.com = "BMW"

c1 = Car()
c2 = Car()

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

c1.wheels = 4.0
c1.mil= 12 
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
