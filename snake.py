from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self,position):
        ns = Turtle()
        ns.shape("square")
        ns.color("white")
        ns.penup()
        ns.goto(position)
        self.segments.append(ns)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            nx = self.segments[seg_num - 1].xcor()
            ny = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(nx, ny)
        self.head.forward(20)
    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)