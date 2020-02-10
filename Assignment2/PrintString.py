#!/bin/python3
def PrintString(mystring):
    final_string = ''
    for i in range(len(mystring)):
        if i % 2 ==0 and mystring[i] != ' ':
            final_string = final_string + mystring[i]
    return final_string
print(PrintString(' p y t h o n'))    

