# import the turtle module
import turtle

# define a variable to hold users color preference
color = input("What is your color preference (red, blue, green)? ")
# redefined the color variable to always lowercase regardless of user input
color = color.lower()

# tell turtle to use the user's color
turtle.fillcolor(color)
# tell turtle to begin filling with that color
turtle.begin_fill()
# draw the shape
turtle.goto(0,50)
turtle.goto(100,50)
turtle.goto(100,0)
turtle.goto(0,0)
# tell turtle to stop filling with that color
turtle.end_fill()
# tell turtle to exit the screen only on click
turtle.exitonclick()