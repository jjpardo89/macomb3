import turtle
import time

#pen and color variables
pen_color = str()
fill_color = str()
pen_size = int()

#Moving the pen
turtle.penup()
turtle.goto(0, 150)
turtle.pendown()

#Two Needed Inputs
pen_size = int(input("Enter the size between the numbers 1-10: "))
pen_color = (input("Determine the color, choose red blue or yellow: "))

#Fill color decision structure
if pen_color == 'red':
    fill_color = 'blue'
elif pen_color == 'blue':
    fill_color = 'red'
elif pen_color == 'yellow':
    fill_color = 'red'
else:
    fill_color = 'yellow'

#Setting the pen size, fill color, and pen color
turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)
turtle.begin_fill()
#draw circle
turtle.circle(50)
#stopping the fill
turtle.end_fill()

#Moving the pen
turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.goto(0,0)
turtle.pendown()

#Ask user for new color
pen_color = (input("Determine the color, choose red blue or yellow: "))

#Fill color decision structure
if pen_color == 'red':
    fill_color = 'yellow'
elif pen_color == 'blue':
    fill_color = 'yellow'
elif pen_color == 'yellow':
    fill_color = 'blue'
else:
    fill_color = 'red'

#Setting the pen size, fill color, and pen color
turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)

turtle.begin_fill()


#drawing a square
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

#stopping the fill
turtle.end_fill()

#Moving the pen
turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.goto(0,-150)
turtle.pendown()

#Ask user for new color
pen_color = (input("Determine the color, choose red blue or yellow: "))

#Fill color decision structure
if pen_color == 'red':
    fill_color = 'yellow'
elif pen_color == 'blue':
    fill_color = 'yellow'
elif pen_color == 'yellow':
    fill_color = 'blue'
else:
    fill_color = 'red'

#Setting the pen size, fill color, and pen color
turtle.pensize(pen_size)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)

turtle.begin_fill()

#drawing the Triangle
turtle.right(35)
turtle.forward(125)
turtle.right(235)
turtle.forward(150)
turtle.left(127)
turtle.forward(130)


turtle.end_fill()


#On My Own / Second Turtle Test
import turtle
import time
time.sleep(3)
turtle.reset()
turtle.setup(600, 600)

#variables
pen_color = str()
fill_color = str()
pen_size = int()
shape = str()
location = str()

#User needs to decide the shape
shape = input("Type a circle or square: ")
location = input("Choose the location you want to start. Type one of the following - TL (TOP LEFT), TR (TOP RIGHT), BR (Bottom Right), or BL (Bottom Left): ")

#Starting with the location
turtle.penup()
if location == 'TL':
    turtle.goto(-150, 150)
    turtle.pensize(3)
elif location == 'TR':
    turtle.goto(150, 150)
    turtle.pensize(5)
elif location == 'BL':
    turtle.goto(-150, -150)
    turtle.pensize(7)
else:
    turtle.goto(100, -150)
    turtle.pensize(9)


#If the user selects a circle
turtle.pendown()
if shape == 'circle':
    pen_color = input("Which color do you want the outline of the circle to be? Choose: RED, BLUE, or YELLOW: ")
    if pen_color == 'red':
        pen_fill = 'DarkSlateBlue'
    elif pen_color == 'blue':
        pen_fill = 'Firebrick'
    elif pen_color == "yellow":
        pen_fill = 'Plum'
    else:
        pen_fill = 'DeepSkyBlue'
#If square was chosen:
if shape == 'square':
    pen_fill = input("Which color do you want to fill the square with? Choose: red, blue, or yellow: ")
    if pen_fill == 'red':
        pen_color = 'turquoise'
    elif pen_fill == 'blue':
        pen_color = 'maroon' 
    elif pen_fill == 'yellow':
        pen_color = 'sandybrown'       
    else:
        pen_color = 'PaleGoldenrod'

turtle.begin_fill()
turtle.pencolor(pen_color)
turtle.fillcolor(pen_fill)
turtle.circle(50)
turtle.end_fill()
turtle.penup()

turtle.begin_fill()
turtle.pencolor(pen_color)
turtle.fillcolor(pen_fill)
turtle.penup()

#drawing a square
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.pendown()



