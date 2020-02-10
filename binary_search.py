#!/bin/python3
pos =-1
def Binary_search(number_list, number):
   lower_bound = 0
   upper_bound = len(number_list)-1
   while lower_bound <= upper_bound:
      mid = (lower_bound + upper_bound)//2
      if number_list[mid] == number:      
          globals()['pos'] = mid
          return True

      elif number < number_list[mid]:
          upper_bound = mid -1

      else:
          lower_bound = mid + 1    
   return False
if Binary_search([1,2,3,4,5,6,100,102,103,909,999,8888,777777,5555555],777777):
   print("found at",pos)
else:
   print("not found")
