#zellige using Python Turtle
#https://en.wikipedihail.org/wiki/Islamic_geometric_patterns
import turtle as hail
hail.shape("arrow")
hail.bgcolor('lavender')
hail.width(3)  
hail.delay(5) #delaying the turtle animation

#Repeating and rotating a polygon shape.
def drawMosaic(color,numberOfSides,size,numberOfRepetitions):
 hail.color(color)
 for i in range(0,numberOfRepetitions):
   for j in range (0,numberOfSides):
     hail.forward(size)
     hail.left(360 / numberOfSides)
   hail.left(360 / numberOfRepetitions)

#Main Program Starts Here
#Mosaic #1
drawMosaic("#0B5CCB",6,100,20)
#Mosaic #2
#drawMosaic("#CB0B3F",5,100,10)
#Mosaic #3
#drawMosaic("#0BCB9D",6,100,6)
#Mosaic #4
#drawMosaic("#FF5733",6,100,15)

hail.done()