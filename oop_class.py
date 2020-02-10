#!/bin/python3
class Computer:
   def config(self):
      print("wow")
      print(self.new_ram, self.new_ram)
   
   def __init__(self, cpu, ram):
      self.new_cpu = cpu
      self.new_ram = ram
      print("Its not Wow")

comp1 = Computer('Amit', 16)
comp2 = Computer('Snehal', 32)


comp1.config()
comp2.config()


