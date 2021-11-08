# input() is a function that allows the user to type something into the console

# define a variable to hold a user's input
user_name = input("What is your name? ")

# print the user's name
print(user_name)

'''
As a default, ALL input is taken in as a string.
When we want to conduct arithmetic operations on variables from input,
we need to typecast the input to whichever type we are dealing with.
'''

# ask the user for their age
user_age = input("What is your age? ") # getting the age as a string
user_age = int(user_age) # typecasting the result in the next line

# OR

second_user_age = int(input("What is your age? ")) # getting the age as a string and typecasting to an int in the same line