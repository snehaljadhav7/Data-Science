"""
Jadhav_hw1.py
(Snehal Jadhav)
(02/1/2020)
"""

import math  # imports math module


def ConvertMiles():
    miles = int(input("Enter a number of miles:"))  # Accepts value from user.
    kilometers = miles * 1.61  # Calculates Kilometers and stores result in kilometers variable.
    print("That is", kilometers, "km")  # Prints the result.


def CalculateBMI():
    weight_pounds = int(input("Enter your weight in pounds:"))  # Accepts weight value from user.
    height_inches = int(input("Enter your height in inches:"))  # Accepts height value from user.
    BMI = 703 * (weight_pounds / (height_inches * height_inches))  # Calculates BMI and stores result in BMI variable.
    print("Your BMI is", round(BMI, 1))  # Prints the result


def ConvertSeconds(seconds):
    hours = seconds // 3600  # Calculates hour and stores value in hours variable.
    minutes = (seconds % 3600) // 60  # Calculates minute and stores value in minutes variable.
    seconds = (seconds % 3600) % 60  # Calculates second and stores value in seconds variable.
    print(hours, 'hours,', minutes, 'minutes,', seconds, 'seconds')  # Prints the result.


def Smores(crackers, marshmallows, chocolates   ):
    crackers = crackers // 2  # Calculates number of smores for given crackers
    marshmallows = marshmallows // 1  # Calculates number of smores for given marshmallows
    chocolates = chocolates // 3  # Calculates number of smores for given chocolates
    return min(crackers, marshmallows, chocolates)  # Returns the minimum value.


print("***Converting Miles to Kilometers***")
ConvertMiles()
print("***Calculating BMI***")
CalculateBMI()
print("***Converting Seconds to Hours and Minutes***")
ConvertSeconds(3601)
ConvertSeconds(10000)
print("***Making Smores***")
print(Smores(5, 1, 9))
print(Smores(10, 5, 14))
