# coding: utf-8
# license: GPLv3

from math import pi, cos, sin, atan
# from solar_vis import *
from solar_model import *
# from solar_input import *

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
        else:
            r_2 = ((body.x - obj.x)**2 + (body.y - obj.y)**2)  # квадрат расстояния между телами

            if body.x - obj.x != 0:
                corner = abs(atan((body.y - obj.y)/(body.x - obj.x)))
            else:
                corner = pi/2

            fx = gravitational_constant * body.m * obj.m * cos(corner) / r_2
            if body.x > obj.x:
                fx *= -1

            fy = gravitational_constant*body.m * obj.m * sin(corner) / r_2
            if body.y > obj.y:
                fy *= -1

            body.Fx += fx
            body.Fy += fy


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ay = body.Fy/body.m
    ax = body.Fx/body.m
    dx = body.Vx*dt + (ax*(dt**2))/2
    body.x += dx
    body.Vx += ax*dt
    dy = body.Vy*dt + (ay*(dt**2))/2
    body.y += dy
    body.Vy += ay*dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
