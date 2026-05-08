"""Memory, puzzle game of number pairs."""

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'marks': [], 'taps': 0}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update marks and hidden tiles based on tap."""
    spot = index(x, y)
    state['taps'] += 1
    marks = state['marks']

    if spot in marks or not hide[spot]:
        return

    marks.append(spot)

    if len(marks) == 2:
        if tiles[marks[0]] == tiles[marks[1]]:
            hide[marks[0]] = False
            hide[marks[1]] = False
            state['marks'] = []
    elif len(marks) == 3:
        state['marks'] = [marks[2]]


def draw():
    """Draw image, tiles, taps count, and winning message."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    for mark in state['marks']:
        if hide[mark]:
            x, y = xy(mark)
            up()
            goto(x + 25, y)
            color('black')
            write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    up()
    goto(-200, 200)
    color('black')
    write('Taps: ' + str(state['taps']), font=('Arial', 16, 'normal'))

    if all(not hidden for hidden in hide):
        goto(-90, 0)
        color('red')
        write('You win!', font=('Arial', 30, 'bold'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
