#!/bin/python3

def bubble_sort(new_list):
   for i in range(len(new_list)-1,0,-1):
      for j in range(i):
         if new_list[j] > new_list[j+1]:
            temp = new_list[j]
            new_list[j] = new_list[j+1]
            new_list[j+1] = temp
         print(new_list)



bubble_sort([1,9,8,3,2,7,6])
