#FRACTAL GEOMETRY
import turtle as hail
import random
hail.bgcolor('lavender')
#Heading
hail.color('grey')
style = ('verdana', 30, 'bold')
hail.pu()
hail.goto (0,240)
hail.write('FRACTAL GEOMETRY', font=style, align='center') #Heading
hail.goto(0,-50)
hail.pd()

colors  = ["#f4d078","#ec6262","#bdd8d8","#9c789b","#8aa8bf","#61814e","#92c374"]  #Colors list
hail.width(14)
length = 5
hail.speed(3)

for count in range(110):
  color = random.choice(colors) 
  hail.forward(length)
  hail.right(135)
  hail.color(color)
  length = length + 5

hail.mainloop()
