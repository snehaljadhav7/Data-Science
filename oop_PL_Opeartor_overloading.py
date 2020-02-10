#!/bin/python3

class Student:
   

   def __init__(self, m1, m2):
      self.m1 = m1
      self.m2 = m2
   def __add__(self, other):
      c = self.m1 + other.m1
      d = self.m2 + other.m2
      s3 = Student(c,d)
      return s3 

   def __gt__(self, other):
      if self.m1 > other.m1:
         return True
      else:False



s1 = Student(10,20)
s2 = Student(19,5)
s3 = s1 + s2

if s1 > s2:
   print("first")
else:
   print("second")

