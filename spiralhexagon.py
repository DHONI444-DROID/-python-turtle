import turtle
hex = turtle.Pen()
colors =["lime","red","blue","orange","yellow","purple"]
turtle.bgcolor("black")
for i in range(360):
    hex.pencolor(colors[i% 6])
    hex.width(i/ 100+1)
    hex.forward(i)
    hex.left(59)
turtle.done()