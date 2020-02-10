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


#!/bin/python3

def RemoveDuplicates(my_list):
    new_list = []
    for element in my_list:
        if element not in new_list:
             new_list.append(element)
    return new_list
print(RemoveDuplicates([1, 1, 'a', 'b', 1, 'a', 'd']))    
print(RemoveDuplicates([1, 2, 'a', [1, 2, 3], 1, 2, 3,[1, 2, 3]])) 

#!/bin/python3
def PrintString(mystring):
    final_string = ''
    for i in range(len(mystring)):
        if i % 2 ==0 and mystring[i] != ' ':
            final_string = final_string + mystring[i]
    return final_string
print(PrintString(' p y t h o n'))    
 
#!/bin/python3
def fibonacci(number):
   i = 1
   prev_prev = 1
   prev = 0
   for num in range(number):
       fibonacci_number = prev_prev + prev
       prev_prev = prev
       prev = fibonacci_number
     
   print(fibonacci_number)
fibonacci(25

print(Collatz(59))    
