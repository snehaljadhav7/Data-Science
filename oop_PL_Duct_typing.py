#!/bin/python3
class Pycharm:
   def execute(self):
      print("Compiling")
      print("Running")

class My:
   def execute(self):
      print("Compiling")
      print("Running")

class Laptop:
   def code(self, ide):
      ide.execute()

idt = My()

lap = Laptop()
lap.code(idt)


