#!/bin/python3
class A:
 
   def featureA(self):
      print("FeatureA")

class B(A):
   def featureB(self):
      print("FeatureB")

class C(B):

   def featureC(self):
      print("FeatureC")

c1 = C()
c1.featureA()
c1.featureB()
c1.featureC()

