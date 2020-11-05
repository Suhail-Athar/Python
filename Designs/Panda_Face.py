# Import turtle package 
import turtle as hail
hail.bgcolor('lavender')
hail.width(2)

# Function to draw the circle
def ring(col, rad): 

	hail.fillcolor(col) 

	hail.begin_fill() 

	# Draw a circle 
	hail.circle(rad) 

	hail.end_fill() 

######################### Main Section ############################ 
# hail.setpos		 --> move turtle to given position 
# ring(color, radius) --> draw a ring of specified color and radius 
################################################################### 

##### Drawing the ears ##### 
# First ear 
hail.up() 
hail.setpos(-35, 95) 
hail.down 
ring('black', 15) 

# Second ear 
hail.up() 
hail.setpos(35, 95) 
hail.down() 
ring('black', 15) 

##### Draw face ##### 
hail.up() 
hail.setpos(0, 35) 
hail.down() 
ring('white', 40) 

##### Drawing eyes(black) ##### 

# Draw first eye 
hail.up() 
hail.setpos(-18, 75) 
hail.down 
ring('black', 8) 

# Draw second eye 
hail.up() 
hail.setpos(18, 75) 
hail.down() 
ring('black', 8) 

##### Drawing eyes(White) ##### 

# First eye 
hail.up() 
hail.setpos(-18, 77) 
hail.down() 
ring('white', 4) 

# Second eye 
hail.up() 
hail.setpos(18, 77) 
hail.down() 
ring('white', 4) 

##### Drawing the nose ##### 
hail.up() 
hail.setpos(0, 55) 
hail.down 
ring('black', 5) 

##### Drawing the mouth ##### 
hail.up() 
hail.setpos(0, 55) 
hail.down() 
hail.right(90) 
hail.circle(5, 180) 
hail.up() 
hail.setpos(0, 55) 
hail.down() 
hail.left(360) 
hail.circle(5, -180) 
hail.hideturtle()

hail.done()
