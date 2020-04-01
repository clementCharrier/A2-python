import turtle
turtle.setup(800,400)

def drawCurve(turtle,l,n):

    if n==0:
        turtle.forward(l)



    else :
        drawCurve(turtle,l,n-1)
        turtle.left(60)
        drawCurve(turtle,l,n-1)
        turtle.right(120)
        drawCurve(turtle,l,n-1)
        turtle.left(60)
        drawCurve(turtle,l,n-1)


def drawCurveFull(turtle,l,n):

    if n==0:
        turtle.forward(l)


    else :
        drawCurve(turtle,l,n)
        turtle.right(120)
        drawCurve(turtle,l,n)
        turtle.right(120)
        drawCurve(turtle,l,n)
        turtle.right(120)






turtle.up()
turtle.goto(-300,0)
turtle.down()
drawCurveFull(turtle,30,3)

turtle.exitonclick()
        # turtle.left(60)
        # drawCurve(turtle,l,n-1)
        # turtle.right(120)
        # drawCurve(turtle,l,n)
        # turtle.left(60)
        # drawCurve(turtle,l,n)
        # turtle.left(60)
        # turtle.left(60)
        # turtle.forward(l/3)
        # turtle.right(120)
        # turtle.forward(l/3)
        # turtle.left(60)
        # turtle.forward(l/3)
        # turtle.left(60)
