# coding: utf-8
# license: GPLv3
import math

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx -= (gravitational_constant * body.m * obj.m * (body.x - obj.x)/r**3)
        body.Fy -= (gravitational_constant * body.m * obj.m * (body.y - obj.y)/r**3)

        # FIXME: обработка аномалий при прохождении одного тела сквозь другое


def move_space_object(body, dt):
    ax = body.Fx/body.m
    ay = body.Fy/body.m
    body.x += body.Vx * dt
    body.Vx += ax * dt
    body.y += body.Vy * dt
    body.Vy += ay * dt


def recalculate_space_objects_positions(space_objects, dt):
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
