# in python, we can access individual characters within strings directly by their position
# positions in strings start from 0
# we call these "positions" indeces, where we access the individual characters by their corresponding index

# for example, if I wanted to access the 2nd character of the phrase "Hello", we would do it like this...
phrase = "Hello"
print(phrase[0]) # output: H
print(phrase[1]) # output: e
print(phrase[2]) # output: l
print(phrase[3]) # output: l
print(phrase[4]) # output: o

# we use bracket notation to directly reference certain characters inside of strings
# note: all strings start from index of 0

# in python, we can also use negative indexing...
# negative indexing refers to the last character and goes forward instead of linear
# i.e -1 is the last character index of a string, -2 is the second to last, etc. 
print(phrase[-1]) # output: o
print(phrase[-2]) # output: l
print(phrase[-3]) # output: l
print(phrase[-4]) # output: e
print(phrase[-5]) # output: H

# the reason why we learn this is because it can help make our formatting easier
name = input("Name: ")
name = name.capitalize()

print(f"Your name is {name}.")