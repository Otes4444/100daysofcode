# To calculate Time of Flight 
# Time of Flight Formula # T =(2(initial velocity) * (sine of launch angle) / (acceleration due to  gravity))
# t = time of flight (s)
# v0 = initial velocity (m/s)
# g = acceleration due to gravity (9.80 m/s2)
# θ = angle of the initial velocity from the horizontal plane (radians or degrees)
import cmath
import math
# from Time of Flight Formula Questions:
v0 = 2.10 
θ = 36.9
g = 9.80
time =  2 * (v0) * math.sin ( math.radians (θ)) / (g)
print("the cricket's time of flight is =", (time))
