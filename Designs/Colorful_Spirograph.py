import turtle as hail

hail.bgcolor('black')
hail.width(2)
hail.speed(10) 

#Repeat six times 
for i in range(6):
	
	# Various color combination
	for color in ('red', 'magenta', 'blue', 
				'cyan', 'green', 'white', 
				'yellow'): 
		hail.color(color) 
		
		# Draw the circle
		hail.circle(100)
		
		# Move 10 units left to draw another circle 
		hail.left(10) 
	
	# Hide the turtle
	hail.hideturtle()
hail.done()