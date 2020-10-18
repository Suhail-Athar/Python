# import turtle 
import turtle as hail

hail.bgcolor('lavender')
# initialising variables 
dist = 1
flag = 300

# changing speed of turtle 
hail.speed(10)
hail.width(2)

# making patten 
while flag: 
    
    # makes the turtle to move forward 
    hail.forward(dist) 
      
    # makes the turtle to move left 
    hail.left(100) 
    hail.left(1) 
    dist += 2
    flag -= 1
  
hail.done() 