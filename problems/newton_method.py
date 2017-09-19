##
# Source: https://tour.golang.org/flowcontrol/8
# Implement the square root function using Newton’s method. In this case, Newton’s method is to 
# approximate sqrt(x) by picking a starting point z and then repeating: 
# z_next = z - ((z*z - x) / (2 * z))
# To begin with, just repeat that calculation 10 times and see how close you get to the answer 
# for various values (1, 2, 3, …). Next, change the loop condition to stop once the value has 
# stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?
##

########## TO DO  ###########
def newton_method(z,x):
    z_next = z - ((z*z - x) / (2 * z))
    return z_next


print(newton_method(2,3))

