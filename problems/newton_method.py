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

#Given an aproximation(z) and the number which we are looking the square root of(x),
# return the next aproximation to the square root of x.
def newton_method(z,x):
    z_next = z - ((z*z - x) / (2 * z))
    return z_next

#Assign values to x (Number we want the square root of) and z(The first aproximation to the sauqre root of x)
x,z= 400000,1.0

#While the aproximation does not match the actual square root loop.
while z != m.sqrt(x):
    #Check wether the values of the aproximation start repeating or not and scape the loop
    if z != newton_method(z,x): 
        z = newton_method(z,x)
        print("Current guess:",z)
    else:
        print("Final guess:",z)
        break
#Print actual square root to compare
print("Square Root:",m.sqrt(x))
