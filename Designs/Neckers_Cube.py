#import the turtle modules 
import turtle as c

#Customizing the turtle 
c.shape("circle")
c.shapesize(1,1)
c.bgcolor("black")
c.width(7)
c.color("white")
c.speed(1)

#Square face 1 
for i in range(4): 
	c.forward(150); c.dot(20, "red") 
	c.left(90) 

#Middle part
c.goto(75,75)

#Square face 2 
for i in range(4): 
	c.forward(150); c.dot(20, "yellow") 
	c.left(90) 

#Bottom right
c.goto(225,75) 
c.goto(150,0) 

#Top right 
c.goto(150,150) 
c.goto(225,225) 

#Top left 
c.goto(75,225) 
c.goto(0,150)

c.done()