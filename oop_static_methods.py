#!/bin/python3

class Student:
   th ="Amit"

   def __init__(self):
      self.m1 = 90

   @classmethod
   def class_method(cls):
      print("Teacher Name", cls.th)

   @staticmethod
   def static_method():
      a =9
      b = 8
      return ("my way", a + b)

print(Student.class_method())
print(Student.static_method())
