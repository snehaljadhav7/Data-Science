#!/bin/python3

def multiplication_table(number):
    for i in range(number):
        for j in range(number):
            print(j)
            print(i,end="")

print(multiplication_table(3))
