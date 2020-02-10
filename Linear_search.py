#!/bin/python3
'''pos = -1

def search(number_list, number):
   i =0
   while i < len(number_list):
      if number == number_list[i]:
         globals()['pos'] = i
         return True
      i = i + 1

if search([1,2,3,4,5,6],0):
   print("found at",pos)
else:
   print("not found")'''

pos = -1

def search(number_list, number):
   i =1
   for ele in range(len(number_list)):
      if number == number_list[ele]:
         globals()['pos'] = ele
         return True

if search([1,2,3,4,5,6],4):
   print("found at",pos)
else:
   print("not found")
