#!/bin/python3

def Collatz(n):
    my_list = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2	
            my_list.append(int(n))
        else:
            n = n * 3 + 1
            my_list.append(int(n))
    return my_list


print(Collatz(59))    
