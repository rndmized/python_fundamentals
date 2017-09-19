
#FizzBuzz Code

i = 0
#Loop from 1 to 101, 101 not being included.
for i in range(1,101): 
    #If i is divisible by 3  
    if i % 3 == 0:
        #Print fizz
        print("Fizz")
    #Else if i is divisible by 5
    elif i % 5 == 0:
        #Print buzz
        print("Buzz")
    #If i is not divisible by 3 nor 5
    else:
        #print i value
        print(i)

