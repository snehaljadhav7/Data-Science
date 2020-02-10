#!/bin/python3
class A:
   
   def show(self):
      print("A is")


class B(A):  
   pass
   #def show(self):
      #sprint("b is")

 
b = B()
print(b.show())
