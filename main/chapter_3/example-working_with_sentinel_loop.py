# ask the user for a color
user_color = input("What is your favorite color? ")

# create the sentinel loop
while user_color != 'red':
    print("The code breaking color, has not been entered.")
    user_color = input("What is your favorite color? ")
print("The code breaking color has been entered.")