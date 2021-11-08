# this py file will be strictly dedicated to "Boolean Logic"
# Boolean Logic is best defined as the combination of phrases that can result in printing different values

# define two variables
a = True
b = False

# if-statement... output: True
# the if condition prints, if the "if statement" evaluates to True
if a:
    print("True")
else:
    print("False")

if b: # output: False
    print("True")
else:
    print("False")

''' 
and: both clauses must be True 
or: one of the clauses must be True
'''

# and-statements... output: Neither
if a and b:
    print("Both")
else:
    print("Neither")

# or-statement... output: Both
if a or b:
    print("Both")
else:
    print("Neither")

# define new variables to demonstrate truth table
x = True
y = True

# output: True
if x and y:
    print("True")
else:
    print("False")

# output: True
if (x and y) or x:
    print("True")
else:
    print("False")

# new reassignment
# x still equals True
y = False

# output: False
if x and y:
    print("True")
else:
    print("False")

# output: True
if x or y:
    print("True")
else:
    print("False")

# output: True
if (x or y) and x:
    print("True")
else:
    print("False")

# output: True
if (x and y) or x:
    print("True")
else:
    print("False")

# output: False
if not x and not y:
    print("True")
else:
    print("False")