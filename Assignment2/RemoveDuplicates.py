#!/bin/python3

def RemoveDuplicates(my_list):
    new_list = []
    for element in my_list:
        if element not in new_list:
             new_list.append(element)
    return new_list
print(RemoveDuplicates([1, 1, 'a', 'b', 1, 'a', 'd']))    
print(RemoveDuplicates([1, 2, 'a', [1, 2, 3], 1, 2, 3,[1, 2, 3]]))  
