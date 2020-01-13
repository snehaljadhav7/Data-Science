#!/bin/python3
import math
weight_pounds = int(input("Enter your weight in pounds:"))
height_inches = int(input("Enter your height in inches:"))

BMI=703*(weight_pounds / (height_inches*height_inches))
print("Your BMI is",round(BMI,1))
