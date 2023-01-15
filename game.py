import turtle

w=turtle.Screen()
w.title("zgm")
w.bgcolor("black")
w.setup(width=900,height=600)
w.tracer(0)
#paddle 1
p1=turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.shapesize(stretch_wid=4, stretch_len=1)
p1.color("white")
p1.penup()
p1.goto(-430,0)

#score
score1=0
score2=0

#pen
pen=turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("white")
pen.goto(0,270)
pen.write("player a =0   player b=0", align="center", font=("Arial", 10, "bold"))
pen.hideturtle()



pen1=turtle.Turtle()
pen1.penup()
pen1.speed(0)
pen1.color("white")
pen1.goto(0,0)
pen1.hideturtle()



p2=turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.shapesize(stretch_wid=4, stretch_len=1)
p2.color("white")
p2.penup()
p2.goto(430,0)

#ball
p3=turtle.Turtle()
p3.speed(0)
p3.shape("square")
p3.color("white")
p3.penup()
p3.goto(0,0)
p3.dx=0.1
p3.dy=-0.1

def p1up():
    y=p1.ycor()
    y=y+15
    p1.sety(y)
def p1d():
    y=p1.ycor()
    y=y-15
    p1.sety(y)

def p2up():
    y=p2.ycor()
    y=y+15
    p2.sety(y)
def p2d():
    y=p2.ycor()
    y=y-15
    p2.sety(y)

def exitas():
    exit()


#listening to keyboard
w.listen()
w.onkeypress(p1up, "w")
w.onkeypress(p1d, "s")
w.onkeypress(p2up, "Up")
w.onkeypress(p2d, "Down")



#main game loop
while True:
    w.update()
    p3.setx(p3.xcor()+p3.dx)
    p3.sety(p3.ycor()+p3.dy)
    if p3.ycor()>290:
        p3.sety(290)
        p3.dy*=-1
    if p3.ycor()<-290:
        p3.sety(-290)
        p3.dy*=-1
    if p3.xcor()>430:
        p3.goto(0,0)
        p3.dx*=-1
        score1+=1
        pen.clear()
        pen.write("player a = {}   player b= {}".format(score1,score2), align="center", font=("Arial", 10, "bold"))
    if p3.xcor()<-430:
        p3.goto(0,0)
        p3.dx*=-1
        score2+=1
        pen.clear()
        pen.write("player a = {}   player b= {}".format(score1,score2), align="center", font=("Arial", 10, "bold"))
    if p3.xcor()>425 and (p3.ycor()<p2.ycor()+40) and (p3.ycor()>p2.ycor()-40):
        p3.dx*=-1
    if p3.xcor()<-425 and (p3.ycor()<p1.ycor()+40) and (p3.ycor()>p1.ycor()-40):
        p3.dx*=-1
    if score1==4:
        pen1.write("player a win", align="center", font=("Ariel", 40, "bold"))
        w.exitonclick()
    elif score2==4:
        pen1.write("player b win", align="center", font=("Ariel", 40, "bold"))
        w.exitonclick()
