from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create()
        self.head=self.snake_segments[0]
        # self.up=self.snake_segments[0].left(90)

    def create(self):
        for i in range(0, 3):
            tim = Turtle()
            tim.penup()
            tim.shape("square")
            tim.color("white")
            tim.goto(-i * 20, 0)
            self.snake_segments.append(tim)

    def grow_length(self):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        last_x=self.snake_segments[-1].xcor()
        last_y = self.snake_segments[-1].ycor()
        tim.goto(last_x,last_y)
        self.snake_segments.append(tim)

    def move(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[i].goto(self.snake_segments[i - 1].xcor(), self.snake_segments[i - 1].ycor())
        self.head.forward(20)

    def reset(self):
        for i in self.snake_segments:
            i.goto(1000,1000)
        self.snake_segments.clear()
        self.create()
        self.head = self.snake_segments[0]

    def up(self):
        angle=self.head.heading()
        if(angle!=270):
            self.head.left(90-angle)

    def down(self):
        angle = self.head.heading()
        if(angle!=90):
            self.head.left(270 - angle)

    def right(self):
        angle = self.head.heading()
        if(angle!=180):
            self.head.left(0-angle)

    def left(self):
        angle = self.head.heading()
        if(angle!=0):
            self.head.left(180 - angle)