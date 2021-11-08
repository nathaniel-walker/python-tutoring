# in python, we control decisions with how a program executes by using "if", "elif", "else" statements
# these statements act as conditions existing in the program that direct the program's flow from one decision to another

# set variable equal to something
color = "red"

# use decision structure - double equals sign is a "comparative operator"
# comparative operator- evaluates the rightward expression in comparison to the leftward variable
if color == "red":
    print("My color is red!")
else:
    print("My color is not red.")


# example 2 - taking user input
password = input("What is your password?")
# define the successful password
success = "NYU"

# implement the decision structure
if password == success:
    print("Login successful.")
else:
    print("Unsuccessful login.")