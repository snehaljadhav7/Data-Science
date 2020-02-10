#!/bin/python3


#!/bin/python3


def min_selection_sort(new_list):
       
   for i in range(len(new_list)-1):
      min = i
      for j in range(i, len(new_list)-1):
         if new_list[j] < new_list[min]:
            min = j
      temp = new_list[i]        
      new_list[i] = new_list[min]
      new_list[min]= temp
      print(new_list)


#!/bin/python3


def selection_sort(new_list):
       
   for i in range((len(new_list))-1,0,-1):
      max = i
      for j in range(i):
         if new_list[j] > new_list[max]:
            max = j
      temp = new_list[i]        
      new_list[i] = new_list[max]
      new_list[max]= temp
      print(new_list)





selection_sort([3,2,1,9,5])






min_selection_sort([3,2,1,4,8,7,6,9])



