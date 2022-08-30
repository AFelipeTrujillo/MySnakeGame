import turtle
from board import *


def main():
    game = SnakeGame(title='My Snake Game')
    game.start()
    game.play()
    turtle.done()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
