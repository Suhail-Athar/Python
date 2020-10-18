import turtle as hail

# Set background color
hail.bgcolor("#4863A0")

# Function to draw body of snowman
def circ_draw(color, radius, a, b):
	hail.penup()
	hail.width(3)
	hail.fillcolor (color)
	hail.goto (a, b)
	hail.pendown()
	hail.begin_fill()
	hail.circle (radius)
	hail.end_fill()
	
#Drawing snowman body
circ_draw ("#ffffff", 62, 0, 40)
circ_draw ("#ffffff", 90, 0, -100)
circ_draw ("#ffffff", 120, 0, -270)

# Drawing the Eyes
circ_draw ("#ffffff", 9, -23, 110)
circ_draw ("#F33C22", 4, -23, 114)

circ_draw ("#ffffff", 9, 23, 110)
circ_draw ("#F33C22", 4, 23, 114)

# Drawing the Nose
circ_draw ("#FF6600", 7, 0, 90)

# Body Buttons
circ_draw ("#1E8449", 5, 0, 45)
circ_draw ("#1E8449", 5, 0, 10)
circ_draw ("#1E8449", 5, 0, -23)

# Function to draw arms
def create_line(a, b, length, angle): 
	hail.penup()
	hail.width(11)
	hail.goto(a, b)
	hail.setheading(angle)
	hail.pendown()
	hail.forward(length)
	hail.setheading(angle +21)
	hail.forward(40)
	hail.penup()
	hail.back(40)
	hail.pendown()
	hail.setheading(angle -21)
	hail.forward(40)
	hail.penup()
	hail.home()

#Arms
create_line(-80, 0, 75, 160)
create_line(80, 0, 75, 20)

#Legs
create_line(-80, -200, 75, 210)
create_line(80, -200, 75, -30)

# Drawing hat
hail.penup()
hail.goto(-70, 145)
hail.pensize(3)
hail.pendown()
hail.fillcolor("maroon")
hail.begin_fill()
hail.goto(70,145)
hail.left(90)
hail.goto(70, 165)
hail.left(90)
hail.goto(40, 165)
hail.left(90)
hail.goto(40, 200)
hail.left(90)
hail.goto(-40,200)
hail.left(90)
hail.goto(-40,165)
hail.right(90)
hail.goto(-70,165)
hail.left(90)
hail.goto(-70,145)
hail.end_fill()
hail.pu()

#Heading
hail.goto(-111,220)
hail.pd()
hail.color('#85C1E9')
hail.write("SNOW-MAN", move=True, font=("Verdana",30, "normal"))
hail.ht()
hail.done()