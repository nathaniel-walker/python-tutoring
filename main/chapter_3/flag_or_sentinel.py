# a flag in programming is purposely setting a condition to trigger a loop's end

# example:
x = True
while x:
    print("The loop is running.")
    x = False

# second example:
ask_again = input("Run again (y/n)? ")
while ask_again == 'y' or ask_again == 'Y':
    print("Looping...")
    ask_again = input("Run again (y/n)? ")