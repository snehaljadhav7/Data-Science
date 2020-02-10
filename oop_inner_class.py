#!/bin/python3
class Student:
   school_name = "XYZ"


   def __init__(self,st):
      print("name",self.school_name,st)
      #self.lap = self.Laptop()
      #self.lap.show()   

   class Laptop:
      
      def __init__(self):
          self.brand = 'HP'
          self.memory = 12

      def show(self):
         print(self.brand, self.memory)


s1 = Student(1)
s2 = Student(2)

print("for both s1 and s2")
lap1 = Student.Laptop()
lap1.show()

print("For s1")
lap2 = s1.Laptop()
lap2.show()

print("For s2")
lap3 = s2.Laptop()
lap3.show()

