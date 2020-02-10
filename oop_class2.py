#!/bin/python3
class Car:
   wheels = 4
  
   def __init__(self):
      self.mil = 56
      self.brand = 'BMW'



c1 = car()
c2 = car













#!/bin/python3
class Computer:
   def __init__(self):
      self.name = "Amit"
      self.age = 30
   
   def update(self):
      self.age = 31
   def compare(self,c2):
      if self.age == c2.age:
         return True
      else:
         return False

c1 = Computer()
c2 = Computer()
c1.update()

if c1.compare(c2):
   print("they are same")
else:
   print("they are not same")

Output:they are same

