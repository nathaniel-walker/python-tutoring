# the turtle module in python is used for computer graphics generation
# we call the turtle module via an import statement at the very top of the document so that we tell python we want to use it

# import statement
import turtle

# think about the screen like an X and Y axis, two dimensional graph

# if we want to go up 50 coordinates on the Y-axis without drawing, we say
turtle.up() # picks up the pen from drawing on the screen
turtle.goto(0,50) # goes to the coordinated (0,50)
turtle.down() # puts the pen back down for drawing on the screen

# draw a green circle from the coordinates we are at (0,50)
turtle.fillcolor('green') # sets the fillcolor() method by passing a string as an argument
turtle.begin_fill() # begins the act of filling in the color for whatever statements proceed this command
radius = 50 # define the radius of the circle
turtle.circle(radius) # pass in the radius to the circle() method as an argument
turtle.end_fill() # stops filling the color for proceeding commands

# we use up and down to transport places on the graph without drawing

turtle.exitonclick() # keeps the turtle window in display and only exits on the user's click

# all documentation on turtle can be found here: https://docs.python.org/3/library/turtle.html