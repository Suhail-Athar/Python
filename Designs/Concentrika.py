import turtle    # importing the module
import random    # importing random module for generating random numbers
hail = turtle.Turtle()    #making a turtle object of Turtle class for drawing
screen=turtle.Screen()    #making a canvas for drawing
screen.setup(420,320)    #choosing the screen size
screen.bgcolor('lavender')    #making canvas black
hail.pensize(10)    #choosing the size of pen nib
hail.speed(1)    #choosing the speed of drawing
hail.shape('turtle')   #choosing the shape of pen nib

n=0
while n<14:
    r=random.randint(1,120)   #random numbers for red
    g=random.randint(81,200)   #random numbers for green
    b=random.randint(61,255)   #random numbers for blue
    turtle.colormode(255)   #declaring the colour mode
    hail.pencolor(r,g,b)   #pen colour
    n=n+1
    hail.penup()
    hail.setpos(0,-n*20)
    hail.pendown()
    hail.circle(20*n)
hail.mainloop()