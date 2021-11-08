# concatenation - adding two or more things together; in Python, we refer to "things" as strings

# basic example using print...
# plus operator combines two strings with no space
print("Hello" + "World!") # output: HelloWorld!
# comma operator combines two strings with added space
print("Hello", "World!") # output: Hello World!

# define some phrases and piece them together
phrase_1 = "The"
phrase_2 = "weather"
phrase_3 = "outside"
phrase_4 = "is"
phrase_5 = "beautiful!"
# printing concatenated variables - no spaces
print(phrase_1 + phrase_2 + phrase_3 + phrase_4 + phrase_5)
# printing concatenated variables - with spaces
print(phrase_1, phrase_2, phrase_3, phrase_4, phrase_5)

''' 
RULES OF CONCATENATION:
    1) strings are the only type that can be concatenated
        1a) if you want to concatenate another type, you MUST convert it to a string
    2) strings are not spaced using plus (+) operators
        2a) we add space between strings using commas or manually at the end of the string
            2aa) i.e print("Hello " + "World!")
            2ab) i.e print("Hello", "World!")
'''