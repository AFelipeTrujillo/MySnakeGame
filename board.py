import time, random
from turtle import Turtle, Screen


class SnakeGame:

    def __init__(self, title, background='black', height=600, width=600):
        self._snake = Snake()
        self._food = Food()
        self._score = Score()
        self._title = title
        self._background = background
        self._height = height
        self._width = width
        self._speed = 0.08
        self._screen = Screen()

    @property
    def snake(self):
        return self._snake

    @snake.setter
    def snake(self, snake):
        self._snake = snake

    @property
    def screen(self):
        return self._screen

    def start(self):
        self._screen.title(self._title)
        self._screen.bgcolor(self._background)
        self._screen.setup(height=self._height, width=self._width)
        self._screen.tracer(0)
        self._screen.listen()
        self._screen.onkeypress(self._snake.head.up, 'Up')
        self._screen.onkeypress(self._snake.head.down, 'Down')
        self._screen.onkeypress(self._snake.head.left, 'Left')
        self._screen.onkeypress(self._snake.head.right, 'Right')

    def play(self):
        while True:
            self._screen.update()

            if self._checkCollisions():
                self._stop()
                self._score.clear()

            if self._checkDistanceHeadAndFood():
                self._snake.addBodyPart()
                self._score.add_score()

            total_of_body_parts = len(self._snake.body)
            for index in range(total_of_body_parts - 1, 0, -1):
                x = self._snake.body[index - 1].turtle.xcor()
                y = self._snake.body[index - 1].turtle.ycor()
                self._snake.body[index].turtle.goto(x, y)
            if total_of_body_parts > 0:
                x = self._snake.head.turtle.xcor()
                y = self._snake.head.turtle.ycor()
                self._snake.body[0].turtle.goto(x, y)

            self._snake.move()
            if self._headCollisions():
                self._stop()
                self._score.clear()
            time.sleep(self._speed)

    def _headCollisions(self):
        for body_part in self._snake.body:
            if body_part.turtle.distance(self._snake.head.turtle) < 20:
                return True
        return False

    def _stop(self):
        time.sleep(1)
        self._snake.head.turtle.goto(0, 0)
        self._snake.head.turtle.direction = 'stop'
        for body_part in self._snake.body:
            body_part.turtle.clear()
            body_part.turtle.hideturtle()
        self._snake.body.clear()

    def _checkCollisions(self):
        if self._snake.head.turtle.xcor() > 280 or self._snake.head.turtle.xcor() < -280 or self._snake.head.turtle.ycor() > 280 or self._snake.head.turtle.ycor() < -280:
            return True
        return False

    def _checkDistanceHeadAndFood(self):
        if self._snake.head.turtle.distance(self._food.turtle) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            self._food.turtle.goto(x, y)
            return True
        return False


class Snake:

    def __init__(self):
        self._head = Head()
        self._body = []

    @property
    def head(self):
        return self._head

    @property
    def body(self):
        return self._body

    def move(self):

        if self._head.direction == 'up':
            y = self._head.turtle.ycor()
            self._head.turtle.sety(y + 20)

        if self._head.direction == 'down':
            y = self._head.turtle.ycor()
            self._head.turtle.sety(y - 20)

        if self._head.direction == 'left':
            x = self._head.turtle.xcor()
            self._head.turtle.setx(x - 20)

        if self._head.direction == 'right':
            x = self._head.turtle.xcor()
            self._head.turtle.setx(x + 20)

    def addBodyPart(self):
        self._body.append(BodyPart())


class Head:

    def __init__(self, shape='square', color='white', direction='stop'):
        self._shape = shape
        self._color = color
        self._direction = direction
        self._turtle = Turtle()
        self._turtle.speed(0)
        self._turtle.shape(shape)
        self._turtle.color(color)
        self._turtle.penup()
        self._turtle.goto(0, 0)

    @property
    def direction(self):
        return self._direction

    @property
    def turtle(self) -> Turtle:
        return self._turtle

    def up(self):
        self._direction = 'up'

    def down(self):
        self._direction = 'down'

    def left(self):
        self._direction = 'left'

    def right(self):
        self._direction = 'right'


class BodyPart:

    def __init__(self):
        self._turtle = Turtle()
        self._turtle.speed(0)
        self._turtle.shape('square')
        self._turtle.color('grey')
        self._turtle.penup()

    @property
    def turtle(self) -> Turtle:
        return self._turtle


class Food:

    def __init__(self, shape='circle', color='red'):
        self._turtle = Turtle()
        self._turtle.speed(0)
        self._turtle.shape(shape)
        self._turtle.color(color)
        self._turtle.penup()
        self._turtle.goto(0, 100)

    @property
    def turtle(self):
        return self._turtle


class Score:

    def __init__(self):
        self._turtle = Turtle()
        self._turtle.speed(0)
        self._turtle.color('white')
        self._turtle.penup()
        self._turtle.goto(0, 260)
        self._turtle.hideturtle()
        self._score = 0
        self._high_score = 0
        self._text = f'Score: {self._score}        High Score: {self._high_score}'
        self._turtle.write(self._text, align='center', font=('Courier', 24, 'normal'))

    @property
    def score(self):
        return self._score

    @property
    def high_score(self):
        return self._high_score

    @score.setter
    def score(self, score):
        self._score = score

    @high_score.setter
    def high_score(self, high_score):
        self._high_score = high_score

    def add_score(self, point = 10):
        self._score += point
        if self._score > self._high_score:
            self._high_score = self._score
        self._update_text()

    def _update_text(self):
        self._turtle.clear()
        self._text = f'Score: {self._score}        High Score: {self._high_score}'
        self._turtle.write(self._text, align='center', font=('Courier', 24, 'normal'))

    def clear(self):
        self._score = 0
        self._update_text()

