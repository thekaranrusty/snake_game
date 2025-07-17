COORDINATES = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle
class Snake:

    def __init__(self):
        self.my_turtle = []
        self.create_snake()
        self.head = self.my_turtle[0]

    def create_snake(self):
        for i in range(3):
            tim = Turtle("square")
            tim.penup()
            tim.color("white")
            tim.goto(COORDINATES[i])
            self.my_turtle.append(tim)

    def move(self):
        for t in range(len(self.my_turtle) - 1, 0, -1):
            x = self.my_turtle[t - 1].xcor()
            y = self.my_turtle[t - 1].ycor()
            self.my_turtle[t].goto(x, y)
        self.head.forward(20)


        #Collision Detection
        hx =self.head.xcor()
        hy =self.head.ycor()

        if hx <= 300 and hx>= -300 and hy <= 290 and hy>= -300 :

            #Tail Collision Detection
            for t in self.my_turtle[1:]:
                if self.head.distance(t) < 10:
                    return 0
            return 1

        else :
            return 0


    def up(self):
        if self.my_turtle[0].heading() != DOWN:
            self.my_turtle[0].setheading(UP)
        else:
            self.move()


    def right(self):
        if self.my_turtle[0].heading() != LEFT:
            self.my_turtle[0].setheading(RIGHT)
        else:
            self.move()


    def down(self):
        if self.my_turtle[0].heading() != UP:
            self.my_turtle[0].setheading(DOWN)
        else:
            self.move()


    def left(self):
        if self.my_turtle[0].heading() != RIGHT:
            self.my_turtle[0].setheading(LEFT)
        else:
            self.move()


    def grow_snake(self):
        l = len(self.my_turtle)
        x = self.my_turtle[l - 1].xcor()
        y = self.my_turtle[l - 1].ycor()
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        tim.goto(x,y)
        self.my_turtle.append(tim)

    def restart(self):
        for i in self.my_turtle:
            i.goto(1110,1110)
        self.my_turtle.clear()
        self.create_snake()
        self.head = self.my_turtle[0]



