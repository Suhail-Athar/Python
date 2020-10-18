# Import required module 
import turtle as hail

# Set background color 
hail.bgcolor("#4863A0")

# Function to draw body of snowman 
def draw_circle(color, radius, x, y): 
	hail.penup()
	hail.width(3)
	hail.fillcolor (color) 
	hail.goto (x, y) 
	hail.pendown() 
	hail.begin_fill() 
	hail.circle (radius) 
	hail.end_fill() 
	
#Drawing snowman body 
draw_circle ("#ffffff", 60, 0, 40) 
draw_circle ("#ffffff", 90, 0, -100) 
draw_circle ("#ffffff", 120, 0, -270) 

# Drawing left eye 
draw_circle ("#ffffff", 8, -22, 110) 
draw_circle ("#ffffff", 8, 22, 110)

# Drawing nose 
draw_circle ("#FF6600", 6, 0, 90)

# Body Buttons 
draw_circle ("#ffffff", 4, 0, 45) 
draw_circle ("#ffffff", 4, 0, 10) 
draw_circle ("#ffffff", 4, 0, -23)

# Function to draw arms 
def create_line(x, y, length, angle): 
	hail.penup()
	hail.width(11)
	hail.goto(x, y) 
	hail.setheading(angle) 
	hail.pendown() 
	hail.forward(length) 
	hail.setheading(angle + 21) 
	hail.forward(40) 
	hail.penup() 
	hail.back(40) 
	hail.pendown() 
	hail.setheading(angle - 21) 
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
hail.goto (-40, 140) 
hail.color ("black") 
hail.width(5) 
hail.pendown() 
hail.goto (45, 140)
#hail.goto (45, 140) 
hail.fillcolor ("#9F000F") 
hail.begin_fill() 
hail.left (90) 
hail.forward (25) 
hail.left (90) 
hail.forward (95) 
hail.left (90) 
hail.forward (25)
hail.left (90)
hail.forward (85)
hail.end_fill()
hail.ht()

hail.done()