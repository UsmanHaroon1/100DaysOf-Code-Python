from turtle import Turtle
INITIAL_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:

    def __init__(self):
        self.segments=[]
        for position in INITIAL_POSITIONS:
            self.segments.append(self.createsnake(position))
        self.head= self.segments[0]

    def createsnake(self,position):
        snake_segment = Turtle('square')
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.goto(position)
        return snake_segment

    def addSegment(self):
        self.segments.append(self.createsnake(self.segments[-1].position()))

    def moveforward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def initial(self):
        self.head.goto(0,0)