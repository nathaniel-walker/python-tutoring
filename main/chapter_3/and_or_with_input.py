# take a user's input on two numbers
num_1 = int(input("Number 1: "))
num_2 = int(input("Number 2: "))

# decision structure
if num_1 == num_2: # the numbers are equal
    print("The numbers are equal.")
elif num_1 > num_2: # number one is larger
    print("Number one is greater than number two.")
elif num_1 < num_2: # number one is smaller (aka number two is larger)
    print("Number two is greater than number one.")

if (num_1 == num_2) and num_1 > 2:
    print("Not only are the numbers the same, but both are greater than 2.")
else:
    print("The numbers may not be the same, but one could be less than or equal to 2.")