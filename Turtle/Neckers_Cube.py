#import the turtle modules 
import turtle as c

# background color green 
c.shape("circle")
c.shapesize(1,1)
c.bgcolor("black")
c.width(7)
c.color("white")

#c.pencolor("yellow")
c.speed(1)

# forming front square face 
for i in range(4): 
	c.forward(150); c.dot(20, "red") 
	c.left(90) 

# bottom left side 
c.goto(75,75)

# forming back square face 
for i in range(4): 
	c.forward(150); c.dot(20, "yellow") 
	c.left(90) 

# bottom right side 
c.goto(225,75) 
c.goto(150,0) 

# top right side 
c.goto(150,150) 
c.goto(225,225) 

# top left side 
c.goto(75,225) 
c.goto(0,150)

c.mainloop()

