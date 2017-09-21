##
# Source: https://tour.golang.org/flowcontrol/8
# Implement the square root function using Newton’s method. In this case, Newton’s method is to 
# approximate sqrt(x) by picking a starting point z and then repeating: 
# z_next = z - ((z*z - x) / (2 * z))
# To begin with, just repeat that calculation 10 times and see how close you get to the answer 
# for various values (1, 2, 3, …). Next, change the loop condition to stop once the value has 
# stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?
##
import math as m

########## TO DO  ###########
def newton_method(z,x):
    z_next = z - ((z*z - x) / (2 * z))
    return z_next


x,z= 30.0,1.0
while z != x:
    if z != newton_method(z,x): 
        z = newton_method(z,x)
    else:
        break
    print("Current guess:",z)
print("Square Root",m.sqrt(x))
