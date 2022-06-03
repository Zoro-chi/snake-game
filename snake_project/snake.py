from turtle import Turtle

STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]



    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        self.full_snake.append(snake)

    def extend(self):
        self.add_part(self.full_snake[-1].position())

    def reset(self):
        for part in self.full_snake:
            part.goto(1000, 1000)
        self.full_snake.clear()
        self.create_snake()
        self.head = self.full_snake[0]

    def move(self):
        for part in range(len(self.full_snake) - 1, 0, -1):
            new_x = self.full_snake[part - 1].xcor()
            new_y = self.full_snake[part - 1].ycor()
            self.full_snake[part].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            left = self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            right = self.head.setheading(RIGHT)
