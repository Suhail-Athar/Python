import turtle as hail
import math
hail.ht()
hail.delay(50)
hail.color("#008080")
hail.width(5)
hail.bgcolor("lavender")
size=200

hail.setheading(90) #towards the top
for i in range(0,6):
  hail.forward(size)
  hail.penup()
  hail.forward(-size)
  hail.left(60)
  hail.pendown()

hail.setheading(90) #towards the top
hail.forward(size)
hail.setheading(215) #towards the left
newSize=size
newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(65))
for i in range(0,30):  
   hail.forward(newSize)
   hail.left(60)
   newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(70))

hail.done()