from sketchpy import canvas

import turtle
t=turtle.Turtle()
obj=canvas.sketch_from_svg("Ram.svg")
t=turtle.Turtle()
t.penup()
t.goto(-60,290)
t.pendown()
t.pencolor("Orange")
t.write("Jai Shree Ram",align="center",font=("Arial",10,"bold"))
obj.draw()
t.hideturtle()
turtle.done()