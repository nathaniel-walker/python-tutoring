# define two boolean variables, x and y, where x is true and y is false
x = True
y = False

# design our decision structure with the and/or conditions, and check output
'''
if x and y:
    print("False")
elif x or y:
    print("True")
'''

# design a truth table changing the values of x and y
# x and y will both start out as true
x = True
y = True

# design the truth table
print(f"X\tY\tX and Y\t\tX or Y\n--------------------------------------")
print(f"True\tTrue\tTrue\t\tTrue")
print(f"True\tFalse\tFalse\t\tTrue")
print(f"False\tTrue\tFalse\t\tTrue")
print(f"False\tFalse\tTrue\t\tFalse")