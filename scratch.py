import turtle

screen =turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')

t_ground=turtle.Turtle()
t_ground.speed(15)
t_ground.fillcolor('white')
t_ground.pencolor('white')


t_ground.hideturtle()
t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.end_fill()

t_ground.penup()
t_ground.goto(-150,-110)
t_ground.pendown()
t_ground.fillcolor('white')
t_ground.begin_fill()
t_ground.circle(65)
t_ground.end_fill()

t_ground.penup()
t_ground.goto(-150,-10)
t_ground.pendown()
t_ground.fillcolor('white')
t_ground.begin_fill()
t_ground.circle(55)
t_ground.end_fill()

#writing merry christmas
t_ground.penup()
t_ground.goto(0,200)
t_ground.pendown()
t_ground.write("MERRY CHRISTMAS",font=("arial",30,"bold"),align="center")
t_ground. penup()



t_ground.penup()
t_ground.goto(-150,80)
t_ground.pendown()
t_ground.fillcolor('white')
t_ground.begin_fill()
t_ground.circle(45)
t_ground.end_fill()
#iglo base
t_ground.penup()
t_ground.goto(150,-250)
t_ground.pendown()
t_ground.fillcolor('white')
t_ground.begin_fill()
t_ground.circle(150)
t_ground.end_fill()

#iglo rectangle
t_ground.penup()
t_ground.goto(150,-130)
t_ground.pendown()
t_ground.fillcolor('lightcyan2')
t_ground.begin_fill()
t_ground.circle(50)
t_ground.end_fill()

t_ground=turtle.Turtle()
t_ground.speed(15)
t_ground.fillcolor('white')
t_ground.pencolor('white')

t_ground.penup()
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.end_fill()

#eye1
t_ground.penup()
t_ground.goto(-165,125)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(5)
t_ground.end_fill()

#eye2
t_ground.penup()
t_ground.goto(-125,125)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(5)
t_ground.end_fill()

#button1
t_ground.penup()
t_ground.goto(-150,65)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(5)
t_ground.end_fill()

#button2
t_ground.penup()
t_ground.goto(-150,35)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(5)
t_ground.end_fill()

#button3
t_ground.penup()
t_ground.goto(-150,5)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(5)
t_ground.end_fill()

#smile dot 1 middle
t_ground.penup()
t_ground.goto(-150,95)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(3)
t_ground.end_fill()



#smile dot 2 middleide
t_ground.penup()
t_ground.goto(-165,98)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(3)
t_ground.end_fill()


#smile dot 3
t_ground.penup()
t_ground.goto(-175,105)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(3)
t_ground.end_fill()

#smile dot 4 other side
t_ground.penup()
t_ground.goto(-125,105)
t_ground.pendown()
t_ground.fillcolor('grey0')
t_ground.begin_fill()
t_ground.circle(3)
t_ground.end_fill()


#nose
t_ground.penup()
t_ground.goto(-150,115)
t_ground.pendown()
t_ground.hideturtle()
t_ground.fillcolor('DarkOrange1')
t_ground.pencolor('DarkOrange2')
t_ground.begin_fill()
t_ground.goto(-150,115)
t_ground.goto(-130,85)

t_ground.goto(-130,115)

t_ground.end_fill()

#last line of code
turtle.done()