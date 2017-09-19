#Factorial digit sum
#Recursive funtion to calculate
def factorial(num):
    #For negative numbers 0 or 1 will return 1
    if num <= 1:
        return 1
    else:
        #If num is greater than 1 multiply num by num-1 recursively until it returns 1(lowest value)
        return num * factorial(num-1)

#Ask user to input a number and asgn value to f
f = input("Please, enter a natural number to calculate factorial from: ")
#Call function passing in f parsed and print the returning value.
print(factorial(int(f)))






    