###### Task 8
###### Write a program which takes 3 digits: a, b, c as input and
###### calculate the roots of a quadratic equation ax^2 + bx + c = 0

import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = b**2 - 4*a*c
x1 = ((-b - math.sqrt(delta))/2*a)
x2 = ((-b + math.sqrt(delta))/2*a)
print("delta =",delta)
print("x1 =",x1," ", "x2 =",x2)

