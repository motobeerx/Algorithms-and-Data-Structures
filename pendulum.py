import graphics as gr
import math as m

SIZE_X = 800
SIZE_Y = 600

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
coords = gr.Point(400, 500)




def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)



def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)
    return circle


def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def phaseShift(k, dk):
    if k == 2*m.pi:
        k = 0
    k += dk
    return k

def pendulumMove(k):
    y = -7.5 * m.sin(2 * 10*k)
    x = 10 * m.sin(10*k + m.pi/2)
    return gr.Point(x,y)







clear_window()
rope = gr.Line(gr.Point(coords.x, coords.y), gr.Point(400,0))
rope.draw(window)
ball = draw_ball(coords)
k = 0
move_point = gr.Point(0,0)
gr.time.sleep(0.5)

while True:

    k = phaseShift(k, m.pi/1000)
    move_point = pendulumMove(k)
    ball.move(move_point.x, move_point.y)

    gr.time.sleep(0.04)
