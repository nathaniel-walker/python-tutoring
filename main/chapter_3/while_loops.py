# a loop in programming is designed to run continuously until either the user tells it to stop, or the programmer programs it to stop

# a while loop runs until a user enters a value to make it stop, or a condition is met that is programmed to make the loop end

# example:
x = 0
while x < 5:
    print(x)
    x += 1

''' 
Loop breakdown:
    1st iteration, we defined x is 0... so, printing x within the loop after the 1st iteration will print 0
    We then add 1 to x
    2nd iteration, x is now 1 because we added 1 to x, so 1 prints
    3rd iteration, x is now 2, because we added 1 to x, so 2 prints
    4th iteration, x is now 3, because we added 1 to x, so 3 prints
    5th iteration, x is now 4, because we added 1 to x, so 4 prints
    There is no 6th iteration... reason being, because x equals 5, and 5 is not less than 5, therefore, the loop ends
    The value of x after the loop is still whatever the last condition within the loop dictates 
        (during our 5th iteration, x was 4, so it ran and printed 4, but then we still added 1, so x is equal to 5 now)
'''