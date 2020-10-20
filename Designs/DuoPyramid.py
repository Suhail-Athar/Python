#Drawing 3-3 Duopyramid with (x,y) coordinates, Author- Mohd Suhail Athar
import turtle as z

#Global Values
z.width(4)
z.bgcolor('lavender')
z.shape('arrow')
z.speed(2)
z.color('#1E8449')
z.write(z.pos(), align='right', font=("Verdana",14, "normal"))

#Hexagon in Making
z.color('black')
for i in range (6):
    z.fd(130)
    z.dot(15, "#5B2C6F")  #For showing vertices
    z.left(60)

#Internal Triangle - Blue
z.color('#5DADE2')
z.goto(0.00,225.17)
z.goto(195.00,112.58)
z.goto(0,0)

#Turtle Pos-1
z.pu()
z.goto(130.00,0.00)
z.color('#1E8449')
z.write(z.pos(), align='left', font=("Verdana",14, "normal"))
z.pd()

#Internal Triangle - Orange
z.color('#ff8735')
z.goto(-65.00,112.58)
z.goto(130.00,225.17)
z.goto(130.00,0.00)

#Turtle Pos-2
z.pu()
z.goto(-65.00,112.58)
z.color('#1E8449')
z.write(z.pos(), align='right', font=("Verdana",14, "normal"))
z.pd()

#Grey Diagonal-1
z.color('#8b8b8b')
z.goto(195.00,112.58)
z.color('#1E8449')
z.write(z.pos(), align='left', font=("Verdana",14, "normal"))

#Turtle Pos-3
z.pu()
z.goto(130.00,225.17)
z.color('#1E8449')
z.write(z.pos(), align='left', font=("Verdana",14, "normal"))
z.pd()

#Grey Diagonal-2
z.color('#8b8b8b')
z.goto(0,0)

#Turtle Pos-4
z.pu()
z.goto(0.00,225.17)
z.color('#1E8449')
z.write(z.pos(), align='right', font=("Verdana",14, "normal"))
z.pd()

#Grey Diagonal-3
z.color('#8b8b8b')
z.goto(130.00,0.00)

#End Caption
z.pu()
z.goto(77,-100)
z.pd()
z.write('3-3 DUO PYRAMID', align='center', font=("Verdana",30, "normal"))

#Hide/End the turtle
z.ht()
z.done()

#For more info on Duopyramid, visit https://en.wikipedia.org/wiki/Duopyramid