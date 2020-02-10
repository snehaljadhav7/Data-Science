#!/bin/python3

class Student:
   teacher_name = "Navin Readdy"

   @classmethod
   def class_method_1(cls):
      print("Teacher Name", cls.teacher_name)

Student.class_method_1()


