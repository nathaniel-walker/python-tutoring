# to format output neatly, we can use the print(f) function given to us by python 3.0+

# define one variable
var_1 = 5

# print this in a phrase using the print(f) function
print(f"There are {var_1} days of the business week.")

''' 
REASONS TO USE print(f) OVER CONCATENATION:
    1) we can directly embed ANY variable types inside of print(f)
        1a) this means we do not have to convert everything to type string
    2) you can directly reference ANY variable inside the print(f) statement
        2a) print(f"Yada yada yada {variable} yada yada.")
            VERSUS
            print("Yada yada yada" + variable + " yada yada.")
'''