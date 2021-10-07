# typecasting - converting a variable from one type to another

'''
Rules of typecasting:
    1) float to int
    2) int to float
    3) float to string
        4) string to float
            * the string can ONLY contain a numeric value *
    5) int to string
        6) string to int
            * the string can ONLY contain a numeric value *
'''

# examples

# 1)
a = 2.99 # set a = 2.99, which is type float
a = int(a) # redefined a as an integer by typecasting a as type int
print(a) # printing a to the console --> 2

print()

#2)
b = 3 # set b = 3, which is type int
b = float(b) # redefined b as a float by typecasting b as type float
print(b) # printing b to the console --> 3.0

print()

'''
We can use the type() function to print the actual variable type.
This is a way of checking what the type of the variable is.
'''

#3)
c = 3.8 # set c = 3.8, which is type float
print(type(c)) # float
c = str(c) # redefined c as a string by typecasting c as type str
print(c) # printing c to the console --> 3.8
print(type(c)) # str

print()

#4) 
d = "5.85" # set d = "5.85", which is type str
print(type(d)) # str
d = float(d) # redefined d as a float by typecasting d as type float
print(d) # printing d to the console --> 5.85
print(type(d)) # float

print()

#5)
e = 7 # set e = 7, which is type int
print(type(e)) # int
e = str(e) # redefined e as a string by typecasting e as type str
print(e) # printing e to the console --> 7
print(type(e)) # str

print()

#6)
f = "9" # set f = "9", which is type str
print(type(f)) # str
f = int(f) # redefined f as an integer by typecasting f as type int
print(f) # printing f to the console --> 9
print(type(f)) # int