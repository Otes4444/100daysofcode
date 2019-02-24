# python prgram to solve for projectiles
# formular to find intial velocity v0 =((acceleration due to  gravity)*(time of flight )) / (2*sine of launch angle*angle of the initial velocity)
# g = acceleration due to gravity (9.80 m/s2)
# t = time of flight (s)
# θ = angle of the initial velocity from the horizontal plane (radians or degrees)
import math
# from Question given:
g = 9.80
t = 3.20
θ = 32.0
v0 = (g * t) / (2 * math.sin(math.radians (θ)))
print("The initial velocity of the javelin is = ", v0)