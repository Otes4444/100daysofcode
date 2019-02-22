# Solve the quadratic equation ax**2 + bx + c = 0
import math
import cmath
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
# calculate the discriminant
d = ( b**2 ) - ( 4 * a *c )
# find the real roots, X1 and X2
X1 = (-b - cmath.sqrt (d)) / (2*a)
X2 = (-b + cmath.sqrt (d))/ (2*a)
print("d is =:", d)
print("X1 is =:", X1)
print("X2 is =:", X2)
