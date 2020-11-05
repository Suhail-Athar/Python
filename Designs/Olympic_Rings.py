import turtle as tr

# set thikness for each ring 
tr.width(8)
tr.bgcolor("#f8f9fa")

tr.color("#0081c8") 
tr.penup() 
tr.goto(-110, -25) 
tr.pendown() 
tr.circle(50) 

tr.color("black") 
tr.penup() 
tr.goto(0, -25) 
tr.pendown() 
tr.circle(50) 

tr.color("#ee334e") 
tr.penup() 
tr.goto(110, -25) 
tr.pendown() 
tr.circle(50) 

tr.color("#fcb131") 
tr.penup() 
tr.goto(-55, -75) 
tr.pendown() 
tr.circle(50) 

tr.color("#00a651") 
tr.penup() 
tr.goto(55, -75) 
tr.pendown() 
tr.circle(50) 

tr.done ()