import random as rnd

#Generate a random number
random_number = rnd.randint(1,100)
#print(random_number)

#Number of tries it takes to the user guessing the number
tries = 0
#previous guess
last_guess = 0
#inputed number
n = 0

#This function checks wether the provided number is larger or smaller
#than the random number and returns the correspondant message to user
#If the number matches it will also print the number of tries.
def check_number(n):
    if n < random_number:
        print("Too small")
    elif n > random_number:
        print("Too large")
    else:
        print("Correct! Numer of tries:", tries)
    return

#let user guess
#While the inputed number does not match the randmon number the loop will continue to run
while n != random_number:
    #print("Number of tries: ", tries )
    n = int(input("Please, enter a guess: "))
    #Call funtion to check number
    check_number(n)
    #Check wheter the input was the same as the previous guess
    if n != last_guess:
        #Increment the number of tries if it isn't
        tries += 1
    #Save the last guessed number to check against it in next iteration
    last_guess = n



