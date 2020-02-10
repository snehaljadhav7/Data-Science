#!/bin/python3

class Student:
   school = "Telusko"

   def __init__(self, m1, m2, m3):
      self.m1 = m1
      self.m2 = m2
      self.m3 = m3



   def avg(self):
      return (self.m1 + self.m2 + self.m3)/3

   def get(self):
      return self.m1

   def set(self, value):
      self.m1 = value
   

s1 = Student(30,30,30)
s2 = Student(30,30,30)

print(s1.get())
print(s1.set(20.4))


print(s1.avg())
print(s2.avg())


print(s1.get())
print(s1.set(20))




