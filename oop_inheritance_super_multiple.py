#!/bin/python3
class A:
  
   def __init__(self):
      print("A init")
   
   def featureA(self):
      print("FeatureA")

   def add(self):
      self.a = 10
      self.b = 10
      print(self.a + self.b)



class B():  

   
   def __init__(self):
      print("B init")

   def featureB(self):
      print("FeatureB")

class C(A,B):

   def __init__(self):
      super().__init__()
      print("C init") 

   def featureC(self):
      super().add()
      print("FeatureC")


a1= A()
b1= B()
c1 = C()
c1.featureA()
c1.featureB()
c1.featureC()

