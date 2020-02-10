#!/bin/python3
class A:
  
   def __init__(self):
      print("A init")
   
   def featureA(self):
      print("FeatureA")



class B(A):  

   
   def __init__(self):
      super().__init__()
      print("B init")

   def featureB(self):
      print("FeatureB")

class C(B):

   def __init__(self):
      super().__init__()
      print("C init") 

   def featureC(self):
      print("FeatureC")


a1= A()
b1= B()
c1 = C()
c1.featureA()
c1.featureB()
c1.featureC()

