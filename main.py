import turtle, time, random

speed = 0.1
score = 0
high_score = 0

myWindow = turtle.Screen()
myWindow.title('My Snake')
myWindow.bgcolor('black')
myWindow.setup(height=600, width=600)
myWindow.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

body = []

text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.goto(0,260)
text.hideturtle()
text.write('Score: 0        High Score: 0', align='center', font= ('Courier', 24, 'normal'))

def up():
    head.direction = 'up'


def down():
    head.direction = 'down'


def left():
    head.direction = 'left'


def right():
    head.direction = 'right'


def mov():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


myWindow.listen()
myWindow.onkeypress(up, 'Up')
myWindow.onkeypress(down, 'Down')
myWindow.onkeypress(left, 'Left')
myWindow.onkeypress(right, 'Right')

while True:
    myWindow.update()

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
        for segment in body:
            segment.clear()
            segment.hideturtle()
        body.clear()
        score = 0
        text.clear()
        text.write(f'Score: {score}        High Score: {high_score}', align='center', font=('Courier', 24, 'normal'))

    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        body.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        text.clear()
        text.write(f'Score: {score}        High Score: {high_score}', align='center', font= ('Courier', 24, 'normal'))

    totalSeg = len(body)
    for index in range(totalSeg - 1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x, y)
    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x, y)

    mov()
    for segment in body:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            for segment in body:
                segment.clear()
                segment.hideturtle()
            body.clear()
            score = 0
            text.clear()
            text.write(f'Score: {score}        High Score: {high_score}', align='center',
                       font=('Courier', 24, 'normal'))
            break

    time.sleep(speed)

turtle.done()
