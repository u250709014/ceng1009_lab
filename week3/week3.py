# width = int(input("enter with: "))
# height = int(input("enter with: "))
# area = width * height
# print("bla bla: ", area)
import math
from calendar import firstweekday

# themilestaken = int(input("the miles that taken: "))
# thegasused = int(input("the gas used: "))
# MPG = thegasused / themilestaken
# print("mpg is: ", MPG)
# print("gas used: ", thegasused)

# fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32)*(5/9)
# print(celsius)

# firstweekday= int(input("enter the day vacation start:"))
# vacationlength=int(input("enter the length of vacation:"))
# thelastday= (firstweekday+vacationlength)%7
# print(int(thelastday))

# r= int(input("radius of an circle:"))
# x= 3.14159
#
# circumference= (2*x*r)

# print("circumference:",circumference )

# birthyear= int(input("birth year:"))
# age= 2026-birthyear
# print("age:",age)

import turtle
t = turtle.Turtle()
a =float(input("Enter the length of square: "))
for _ in range(4):
    t.forward(a)
    t.right(90)
turtle.done()