#!/bin/python3

a =5
b =0
k = 'strt'
try:
   c = a/b
   print(c)
   print(int(k))


except ZeroDivisionError as e :
   print("Cannot do this dude", e)

except ValueError as e:
   print("use int", e)

except Exception as e:
   print("Somethin went wrong")

finally :
   print("Everything is closed")
