import turtle
t=turtle.Turtle()
def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polyline(t,10,100,720)