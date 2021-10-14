# in python, we might want to capture something that a user types into the keyboard to interact with them
# we do this via the input() function

# define a variable that takes in the user's name
name = input("What is your name? ")

# print the name back to the user (using print(f))
print(f"Your name is {name}.")

# we can also intake multiple inputs (by making multiple variables for input)
age = input("How old are you? ")
gender = input("What is your biological sex? ")

# print the entirety of what we have captured as one concatenated phrase
print(f"Your name is {name} and you are {age} years old and also a {gender}.")

# if we wanted to get fancy with things...
# we can make sure that all output aligns with EXACTLY the type of formatting we want regardless of user input

# define new variables
name_2 = input("Name: ")
age_2 = input("Age: ")
gender_2 = input("Gender: ")

# print the formatted output as one phrase
print(f"Name is {name_2}, age is {age_2}, gender is {gender_2.lower()}.") # we use the .lower() method to lowercase the input

# function review - 
# .lower() makes an entire variable lowercase
# .upper() makes an entire variable uppercase