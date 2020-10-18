# Import turtle package 
import turtle as hail
hail.bgcolor('lavender')
hail.width(2)

# Defining method to draw a colored circle 
# with a dynamic radius 
def ring(col, rad): 

	# Set the fill 
	hail.fillcolor(col) 

	# Start filling the color 
	hail.begin_fill() 

	# Draw a circle 
	hail.circle(rad) 

	# Ending the filling of the color 
	hail.end_fill() 

##########################Main Section############################# 

# hail.up			 --> move turtle to air 
# hail.down		 --> move turtle to ground 
# hail.setpos		 --> move turtle to given position 
# ring(color, radius) --> draw a ring of specified color and radius 
################################################################### 

##### Draw ears ##### 
# Draw first ear 
hail.up() 
hail.setpos(-35, 95) 
hail.down 
ring('black', 15) 

# Draw second ear 
hail.up() 
hail.setpos(35, 95) 
hail.down() 
ring('black', 15) 

##### Draw face ##### 
hail.up() 
hail.setpos(0, 35) 
hail.down() 
ring('white', 40) 

##### Draw eyes black ##### 

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

##### Draw eyes white ##### 

# Draw first eye 
hail.up() 
hail.setpos(-18, 77) 
hail.down() 
ring('white', 4) 

# Draw second eye 
hail.up() 
hail.setpos(18, 77) 
hail.down() 
ring('white', 4) 

##### Draw nose ##### 
hail.up() 
hail.setpos(0, 55) 
hail.down 
ring('black', 5) 

##### Draw mouth ##### 
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

hail.mainloop()