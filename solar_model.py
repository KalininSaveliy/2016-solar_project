# coding: utf-8
# license: GPLv3
import math
from solar_vis import *
from solar_model import *
from solar_input import *

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        if body.x - obj.x != 0:
            corner = math.atan((body.y - obj.y)/(body.x - obj.x))
        else:
            corner = math.pi/2
        body.Fx += 1  # FIX: нужно вывести формулу...#исправлено
        Fx = gravitational_constant*body.m*obj.m*math.cos(corner)/r**2
        body.Fy += 2  # FIX: нужно вывести формулу...#исправлено
        Fy = gravitational_constant*body.m*obj.m*math.sin(corner)/r**2


def move_space_object(space, body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ay = body.Fy/body.m
    ax = body.Fx/body.m
    # FIX: не понимаю как менять...
    dx = body.Vx*dt + (ax*dt**2)/2
    body.x += dx
    body.Vx += ax*dt
    # FIX: not done recalculation of y coordinate!
    dy = body.Vy*dt + (ay*dt**2)/2
    body.y += dy
    body.Vy += ay*dt
    space.move(body.image, dx, dy)
    print("I'm hero")


def recalculate_space_objects_positions(space, space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(space, body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
