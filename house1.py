from turtle import *

#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("red")


left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120) 
end_fill()
penup()
goto(200,200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# draw a window
penup()
goto(140,140)
pendown()
right(60)
begin_fill()
color("blue")
backward(40)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
penup()
right(90)
forward(90)
pendown()
begin_fill()
color("blue")
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
exitonclick()